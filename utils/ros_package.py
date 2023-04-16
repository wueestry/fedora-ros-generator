import re
import textwrap
from typing import Dict, cast

import yaml
from defusedxml import ElementTree
from rosinstall_generator import generator


class RosPkg:
    def __init__(self, name, distro, pkg_resolver) -> None:
        self.resolver = pkg_resolver
        self.rosdistro = distro
        self.name = name
        self.spec = ""

        self.distro_info = generator.get_wet_distro(distro)
        xml_string = self.distro_info.get_release_package_xml(name)
        self.xml = ElementTree.fromstring(xml_string)
        self.build_deps: Dict[str, set] = {"ros": set(), "system": set()}
        self.run_deps: Dict[str, set] = {"ros": set(), "system": set()}
        self.devel_deps: Dict[str, set] = {"ros": set(), "system": set()}

        try:
            common_config = cast(dict, yaml.load(open("cfg/common.yaml"), Loader=yaml.FullLoader))
        except FileNotFoundError:
            common_config = {}

        try:
            pkg_specific_config = cast(
                dict, yaml.load(open(f"cfg/{self.name}.yaml", "r"), Loader=yaml.FullLoader)
            )
        except FileNotFoundError:
            pkg_specific_config = {}

        self.pkg_config = {**common_config, **pkg_specific_config}
        self.release = self.pkg_config.get("release", 1)

        self.deps_mapping = {
            "build_depend": [self.build_deps],
            "test_depend": [self.build_deps],
            "run_depend": [self.run_deps],
            "buildtool_depend": [self.build_deps, self.devel_deps],
            "build_export_depend": [self.build_deps, self.devel_deps],
            "buildtool_export_depend": [self.build_deps, self.devel_deps],
            "depend": [self.run_deps, self.build_deps],
            "exec_depend": [self.run_deps],
        }
        self.compute_dependencies()

    def compute_dependencies(self) -> None:
        for child in self.xml:
            for dep_key, dep_lists in self.deps_mapping.items():
                if child.tag == dep_key:
                    pkg = child.text
                    try:
                        self.distro_info.get_release_package_xml(pkg)
                        for dep_list in dep_lists:
                            dep_list["ros"].add(pkg)
                    except KeyError:
                        try:
                            dep = self.pkg_config["common"]["dependencies"]["distro_names"][pkg]
                            for dep_list in dep_lists:
                                dep_list["system"].add(dep)
                        except KeyError:
                            system_pkg = self.resolver.get_system_package_name(pkg, self.rosdistro)
                            for dep_list in dep_lists:
                                dep_list["system"].add(system_pkg)

    def get_dependencies_from_cfg(self, dependency_type) -> Dict[str, set]:
        try:
            deps = self.pkg_config["dependencies"][dependency_type]
        except KeyError:
            deps = {}
        for key, val in deps.items():
            deps[key] = set(val)
        return deps

    def translate_dependencies(self, dep_type, dependencies) -> Dict[str, set]:
        """Translate a dependency from ROS' package.xml into a user-defined dep.
        This allows to use system replacements, e.g., by translating the ROS
        package opencv3 to the system package opencv."""
        try:
            translations = self.pkg_config["common"]["dependencies"][dep_type]["translate"]
        except KeyError:
            translations = []
        new_dependencies: Dict[str, set] = {"ros": set(), "system": set()}
        for from_type, from_pkgs in dependencies.items():
            for from_pkg in from_pkgs:
                translated = False
                for translation in translations:
                    if (
                        translation["from"]["type"] == from_type
                        and translation["from"]["pkg"] == from_pkg
                    ):
                        new_dependencies[translation["to"]["type"]].add(translation["to"]["pkg"])
                        translated = True
                        break
                if not translated:
                    new_dependencies[from_type].add(from_pkg)
        new_dependencies["system"] = self.translate_python_dependencies(new_dependencies["system"])
        return new_dependencies

    def translate_python_dependencies(self, dependencies) -> set:
        """For a set of dependencies, translate all python packages to python3 packages."""
        translated_dependencies = set()
        for dep in dependencies:
            new_dep = re.sub("python2?((?=-)|$)", "python3", dep)
            translated_dependencies.add(new_dep)
        return translated_dependencies

    def get_build_dependencies(self) -> Dict[str, set]:
        build_deps = {}
        for key, val in self.build_deps.items():
            build_deps[key] = val | self.get_dependencies_from_cfg("build").get(key, set())
            build_deps[key] -= self.get_dependencies_from_cfg("exclude_build").get(key, set())
        build_deps = self.translate_dependencies("build", build_deps)
        if self.name != "catkin":
            build_deps["ros"].add("catkin")
        return build_deps

    def get_run_dependencies(self) -> Dict[str, set]:
        run_deps = {}
        for key, val in self.run_deps.items():
            # merge with additional dependencies from the config
            run_deps[key] = val | self.get_dependencies_from_cfg("run").get(key, set())
            # remove dependencies excluded in the config
            run_deps[key] -= self.get_dependencies_from_cfg("exclude_run").get(key, set())
            # remove all devel packages
            run_deps[key] -= set([dep for dep in run_deps[key] if re.match(".*-devel", dep)])
        run_deps = self.translate_dependencies("run", run_deps)
        return run_deps

    def get_devel_dependencies(self) -> Dict[str, set]:
        devel_deps = {}
        for key, val in self.devel_deps.items():
            # merge with additional dependencies from the config
            devel_deps[key] = val | self.get_dependencies_from_cfg("devel").get(key, set())
            # remove dependencies excluded in the config
            devel_deps[key] -= self.get_dependencies_from_cfg("exclude_devel").get(key, set())
        devel_deps = self.translate_dependencies("devel", devel_deps)
        return devel_deps

    def get_sources(self) -> list:
        try:
            sources = self.pkg_config["sources"]
        except KeyError:
            sources = []

        ros_pkg = generator.generate_rosinstall(
            self.rosdistro, [self.name], deps=False, wet_only=True, tar=True
        )
        sources.append(ros_pkg[0]["tar"]["uri"])
        return sources

    def get_version(self):
        ros_pkg = generator.generate_rosinstall(
            self.rosdistro, [self.name], deps=False, wet_only=True, tar=True
        )
        return re.match("[\w-]*-([0-9-_.]*)(-[0-9-]*)", ros_pkg[0]["tar"]["version"]).group(1)

    def set_release(self, release):
        self.release = release

    def get_release(self):
        return self.release

    def get_license(self):
        return self.xml.find("license").text

    def get_website(self) -> str:
        for url in self.xml.findall("url"):
            if url.get("type") == "website":
                return url.text
        return "http://www.ros.org/"

    def get_description(self):
        return textwrap.fill(
            self.xml.find("description").text or f"ROS {self.rosdistro} package {self.name}."
        )

    def is_noarch(self):
        return self.pkg_config.get("noarch", False)

    def has_devel(self):
        """Returns True iff the package is a devel package."""
        if "split_devel" in self.pkg_config.keys():
            return self.pkg_config["split_devel"]
        else:
            return True

    def get_patches(self):
        return self.pkg_config.get("patches", [])

    def get_build_flags(self):
        return self.pkg_config.get("build_flags", "")

    def has_no_debug(self):
        return self.pkg_config.get("no_debug", False)
