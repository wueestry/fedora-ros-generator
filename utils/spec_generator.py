import multiprocessing
import os
import queue
import threading
import time
from typing import Dict, List

import jinja2

from utils.package_resolver import PkgResolver
from utils.ros_package import RosPkg
from utils.spec_utils import get_changelog_from_spec, get_version_from_spec
from utils.rosdistros import ros


class SpecFileGenerator:
    def __init__(
        self,
        distro: str,
        bump_release: bool,
        release_version: str,
        user_string: str,
        changelog_entry: str,
        recursive: bool,
        only_new: bool,
        obsolete_distro_pkg: bool,
        destination: str,
    ) -> None:
        self.distro = distro
        self.bump_release = bump_release
        self.release_version = release_version
        self.user_string = user_string
        self.changelog_entry = changelog_entry
        self.recursive = recursive
        self.only_new = only_new
        self.obsolete_distro_pkg = obsolete_distro_pkg
        self.destination = destination

        self.pkg_resolver = PkgResolver()
        self.jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader("templates"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.print_lock = threading.Lock()
        self.packages: List[str] = []
        self.package_queue = queue.Queue()
        self.generated_packages: Dict[str, set] = {}
        self.packages_lock = threading.Lock()

    def tprint(self, msg: str) -> None:
        """Multi-threaded print."""
        self.print_lock.acquire()
        print(msg)
        self.print_lock.release()

    def generate(self, packages: list) -> Dict[str, str]:
        self.packages = packages
        for i in range(multiprocessing.cpu_count()):
            threading.Thread(target=self.worker, daemon=True).start()
        for pkg in packages:
            self.package_queue.put(pkg)
        self.package_queue.join()
        assert len(self.packages) == len(self.generated_packages)
        return self.generated_packages

    def worker(self) -> None:
        while True:
            pkg = self.package_queue.get()
            self.generate_spec_file(pkg)
            self.package_queue.task_done()

    def generate_spec_file(self, package: str) -> RosPkg:
        self.tprint(f"Generating Spec file for {package}.")
        ros_pkg = RosPkg(package, distro=self.distro, pkg_resolver=self.pkg_resolver)
        build_deps = ros_pkg.get_build_dependencies()
        run_deps = ros_pkg.get_run_dependencies()
        devel_deps = ros_pkg.get_devel_dependencies()
        ros_deps = ros_pkg.get_ros_dependencies()

        if self.recursive:
            self.packages_lock.acquire()
            deps = [dep for dep in ros_deps if not dep in self.packages]
            for dep in deps:
                self.package_queue.put(dep)
                self.packages.append(dep)
            self.packages_lock.release()
        sources = ros_pkg.get_sources()
        version = ros_pkg.get_version()
        outfile = os.path.join(
            self.destination, f"ros-{self.distro}-{ros_pkg.name}.spec"
        )
        meta_outfile = os.path.join(self.destination,f'{ros_pkg.name.replace("_", "-")}')
        ros_pkg.spec = outfile
        ros_pkg.meta_spec = meta_outfile
        pkg_changelog_entry = self.changelog_entry

        if os.path.isfile(outfile):
            if self.only_new:
                self.tprint(f"Skipping {ros_pkg.name}, SPEC file exists.")
                return ros_pkg
            changelog = get_changelog_from_spec(outfile)
            if not self.release_version:
                # Release is not specified and Spec file exists, use new version
                # or bump release if it is the same version.
                version_info = get_version_from_spec(outfile)
                if version_info["version"] == f"{version}":
                    pkg_release_version = int(version_info["release"])
                    if self.bump_release:
                        assert pkg_changelog_entry, "Please provide a changelog entry."
                        pkg_release_version += 1
                    else:
                        pkg_changelog_entry = ""
                    ros_pkg.set_release(pkg_release_version)
                else:
                    assert pkg_changelog_entry, "Please provide a changelog entry."
                    ros_pkg.set_release(1)
        else:
            changelog = ""
            assert pkg_changelog_entry, "Please provide a changelog entry."

        try:
            if self.distro in ros:
                spec_template = self.jinja_env.get_template(f"{ros_pkg.name}.spec.j2")
            else:
                spec_template = self.jinja_env.get_template(
                    f"ros2-{ros_pkg.name}.spec.j2"
                )

        except jinja2.exceptions.TemplateNotFound:
            if self.distro in ros:
                spec_template = self.jinja_env.get_template("pkg.spec.j2")
            else:
                spec_template = self.jinja_env.get_template("ros2-pkg.spec.j2")
        
        meta_spec_template = self.jinja_env.get_template('meta_pkg.spec.j2')
        spec = spec_template.render(
            pkg_name=ros_pkg.name,
            distro=self.distro,
            pkg_version=version,
            license=ros_pkg.get_license(),
            pkg_url=ros_pkg.get_website(),
            source_urls=sources,
            build_dependencies=build_deps,
            run_dependencies=run_deps,
            run_dependencies_devel=devel_deps,
            pkg_description=ros_pkg.get_description(),
            pkg_release=ros_pkg.get_release(),
            user_string=self.user_string,
            date=time.strftime("%a %d %b %Y", time.gmtime()),
            changelog=changelog,
            changelog_entry=pkg_changelog_entry,
            noarch=ros_pkg.is_noarch(),
            obsolete_distro_pkg=self.obsolete_distro_pkg,
            has_devel=ros_pkg.has_devel(),
            patches=ros_pkg.get_patches(),
            build_flags=ros_pkg.get_build_flags(),
            no_debug=ros_pkg.has_no_debug(),
        )
        meta_spec = meta_spec_template.render(
            meta_name=ros_pkg.name.replace('_', '-'),
            pkg_name=ros_pkg.name,
            distro=self.distro,
            pkg_version=version,
            license=ros_pkg.get_license(),
            pkg_url=ros_pkg.get_website(),
            pkg_description=ros_pkg.get_description(),
            pkg_release=ros_pkg.get_release(),
            user_string=self.user_string,
            date=time.strftime("%a %d %b %Y", time.gmtime()),
            changelog=changelog,
            changelog_entry=pkg_changelog_entry,
            noarch=ros_pkg.is_noarch(),
            obsolete_distro_pkg=self.obsolete_distro_pkg,
            has_devel=ros_pkg.has_devel()
        )
        with open(outfile, "w") as spec_file:
            spec_file.write(spec)
        with open(meta_outfile, 'w') as meta_spec_file:
            meta_spec_file.write(meta_spec)
        self.packages_lock.acquire()
        self.generated_packages[ros_pkg.name] = ros_pkg
        self.packages_lock.release()
        return ros_pkg
