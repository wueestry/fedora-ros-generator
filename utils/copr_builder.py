import functools
import re
import time

import copr.v3
from termcolor import cprint

from utils.build_node import Node
from utils.build_state import BuildState
from utils.build_tree import Tree
from utils.srpm_builder import SrpmBuilder


class CoprBuilder:
    def __init__(self, copr_owner: str, copr_project: str) -> None:
        """Initialize the CoprBuilder using the given project ID.

        Args:
            copr_owner: the owner of the COPR project
            copr_project: the name of the COPR project
        """
        self.owner = copr_owner
        self.project = copr_project
        self.copr_client = copr.v3.Client.create_from_config_file()
        self.srpm_builder = SrpmBuilder()

    def build_spec(self, chroot: str, spec: str, wait_for_completion: bool = False) -> list:
        """Build a package in COPR from a SPEC.

        Args:
            chroot: The chroot to use for the build, e.g., fedora-26-x86_64
            spec: The path to the SPEC file of the package.
            wait_for_completion: If set to true, wait for the build to finish

        Returns:
            The build object created for this build.
        """
        return self.build_srpm(
            chroot, self.srpm_builder.build_spec(chroot, spec), wait_for_completion
        )

    def build_srpm(self, chroot: str, srpm: str, wait_for_completion: bool) -> list:
        """Build a package in COPR from a SRPM.

        Args:
            chroot: The chroot to use for the build, e.g., fedora-26-x86_64
            srpm: The path to the SRPM file of the package.
            wait_for_completion: If set to true, wait for the build to finish

        Returns:
            The build object created for this build.
        """
        print(f"Building {srpm} for project {self.owner}/{self.project} with chroot {chroot}")
        build = self.copr_client.build_proxy.create_from_file(
            ownername=self.owner,
            projectname=self.project,
            path=srpm,
            buildopts={"chroots": [chroot]},
        )
        assert build, f'COPR client returned build object "{build}"'
        if wait_for_completion:
            self.wait_for_completion([build])
            assert build.state == "succeeded", f"Build failed, state is {build.state}."
            cprint(f"Building {srpm} was successful.", "green")
        return build

    def get_node_of_build(self, nodes: list, build_id: int) -> Node:
        for node in nodes:
            if node.build_id == build_id:
                return node
        raise Exception(f"Could not find node of build {build_id} in build tree")

    def build_tree(self, chroot: str, tree: Tree, only_new: bool = False) -> bool:
        """Build a set of packages in order of dependencies."""
        build_ids = []
        while not tree.is_built():
            wait_for_build = True
            leaves = tree.get_build_leaves()
            print(f"Found {len(leaves)} leave node(s)")
            if not build_ids and not leaves:
                cprint("No pending builds and no leave packages, abort.", "red")
                return False
            for node in leaves:
                if only_new:
                    pkg_version = None
                else:
                    pkg_version = node.pkg.get_version_release()
                if self.pkg_is_built(chroot, node.pkg.get_full_name(), pkg_version):
                    node.state = BuildState.SUCCEEDED
                    build_progress = tree.get_build_progress()
                    cprint(
                        f'{build_progress["building"]}/{build_progress["finished"]}/{build_progress["total"]}: {node.name} is already built, skipping!',
                        "green",
                    )
                    wait_for_build = False
                else:
                    assert (
                        node.state == BuildState.PENDING
                    ), f"Unexpected build state {node.state} of package node {node.name}"
                    build = self.build_spec(chroot=chroot, spec=node.pkg.spec)
                    node.build_id = build.id
                    node.state = BuildState.BUILDING
                    build_ids.append(node.build_id)
            if not wait_for_build:
                continue
            print("Waiting for a build to finish...")
            finished_build = self.wait_for_one_build(build_ids)
            node = self.get_node_of_build(tree.nodes.values(), finished_build.id)
            build_ids.remove(finished_build.id)
            if finished_build.state == "succeeded":
                node.state = BuildState.SUCCEEDED
                build_progress = tree.get_build_progress()
                cprint(
                    f'{build_progress["building"]}/{build_progress["finished"]}/{build_progress["total"]}: Successful build: {node.name}',
                    "green",
                )
            else:
                node.state = BuildState.FAILED
                build_progress = tree.get_build_progress()
                cprint(
                    f'{build_progress["building"]}/{build_progress["finished"]}/{build_progress["total"]}: Failed build: {node.name}',
                    "red",
                )
        return tree.is_built()

    @functools.lru_cache(16)
    def get_builds(self) -> list:
        return self.copr_client.build_proxy.get_list(self.owner, self.project)

    def pkg_is_built(self, chroot: str, pkg_name: str, pkg_version: str) -> bool:
        """Check if the given package is already built in the COPR.

        Args:
            chroot: The chroot to check, e.g., fedora-26-x86_64.
            pkg_name: The name of the package to look for.
            pkg_version: Check for the given version in format $version-$release

        Returns:
            True iff the package was already built in the project and chroot.
        """
        for build in self.copr_client.build_proxy.get_list(self.owner, self.project, pkg_name):
            if build.state != "succeeded":
                continue
            if chroot not in build.chroots:
                continue
            build_version = re.fullmatch(
                "(.+?)(?:\.(?:fc|rhel|epel|el)\d+)?", build["source_package"]["version"]
            ).group(1)
            if build_version == pkg_version:
                return True
        return False

    def wait_for_completion(self, builds: list) -> None:
        """Wait until all given builds are finished.

        Args:
            builds: A list of builds to wait for.
        """
        print(f"Waiting for {len(builds)} build(s) to complete...")
        finished = wait(builds)

    def wait_for_one_build(self, build_ids: int) -> list:
        """Wait for one of the given builds to complete.

        Args:
            build_ids: A list of COPR build IDs.
        Returns:
            The build that completed.
        """
        while True:
            for build_id in build_ids:
                try:
                    build = self.copr_client.build_proxy.get(build_id)
                    if build.state in ["succeeded", "failed", "canceled", "cancelled"]:
                        return build
                except copr.v3.CoprRequestException:
                    print("No connection to copr. Trying again")
                    time.sleep(1)
