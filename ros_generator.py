#! /usr/bin/env python3

import argparse
import os
import subprocess
import sys

from utils.build_order import get_build_order
from utils.build_tree import Tree
from utils.copr_builder import CoprBuilder
from utils.spec_generator import SpecFileGenerator
from utils.srpm_builder import SrpmBuilder


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Spec files for ROS packages with the rosinstall_generator"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default=False,
        help="Generate spec files of dependencies recursively",
    )
    parser.add_argument(
        "-D", "--distro", default="humble", help="ROS distro (default: %(default)s)"
    )
    parser.add_argument(
        "-t",
        "--template",
        default="templates/pkg.spec.j2",
        help="Path to the default Jinja template to generate spec files",
    )
    parser.add_argument(
        "-U",
        "--user_string",
        default="",
        help="User string to use in changelog",
    )
    parser.add_argument(
        "--bump-release",
        default=False,
        action="store_true",
        help="Bump release version of all generated specs by +1",
    )
    parser.add_argument(
        "-v",
        "--release-version",
        default="",
        help="Set a release version of all generated specs",
    )
    parser.add_argument(
        "-d",
        "--destination",
        default="./specs",
        help="Directory where generated spec files are saved",
    )
    parser.add_argument(
        "--distro-specific-specs",
        default=True,
        help="Divide spec files of different distros into seperate subfolders"
    )
    parser.add_argument(
        "-c", "--changelog", type=str, default="", help="Set new changelog entry"
    )
    build_args = parser.add_argument_group("build arguments")
    build_args.add_argument(
        "-b",
        "--build",
        action="store_true",
        default=False,
        help="Build the generated spec file",
    )
    build_args.add_argument(
        "--build-srpm", action="store_true", default=False, help="Generate a SRPM"
    )
    build_args.add_argument(
        "-o",
        "--copr-owner",
        type=str,
        help="Owner of the build COPR project",
    )
    build_args.add_argument(
        "-p", "--copr-project", type=str, help="COPR build project name"
    )
    build_args.add_argument(
        "--chroot",
        action="append",
        type=str,
        help="Chroot used to build packages. Useage of multiple --chroot flags allowed for multiple chroots",
    )
    parser.add_argument(
        "-B",
        "--build-order-file",
        type=argparse.FileType("w"),
        default=None,
        help="Print order in which the packages should be built, requires recursive flag [-r]",
    )
    parser.add_argument(
        "--only-new",
        action="store_true",
        help="Only build packages not present in repo",
    )
    parser.add_argument(
        "--no-obsolete-distro-pkg",
        dest="obsolete_distro_pkg",
        action="store_false",
        help="No obsolete distro-specific package, e.g., ros-kinetic-catkin",
    )
    parser.add_argument("ros_pkg", nargs="+", help="ROS package name")
    args = parser.parse_args()

    if args.distro_specific_specs:
        args.destination = os.path.join(args.destination, args.distro)

    os.makedirs(args.destination, exist_ok=True)

    if not args.user_string:
        user_string = subprocess.run(
            ["rpmdev-packager"], stderr=subprocess.DEVNULL, stdout=subprocess.PIPE
        ).stdout
        if sys.version_info[0] > 2:
            user_string = user_string.decode(errors="replace")
        args.user_string = user_string.strip()

    spec_file_generator = SpecFileGenerator(
        args.distro,
        args.bump_release,
        args.release_version,
        args.user_string,
        args.changelog,
        args.recursive,
        args.only_new,
        args.obsolete_distro_pkg,
        args.destination,
    )
    packages = spec_file_generator.generate(args.ros_pkg)
    if args.build_order_file:
        order = get_build_order(packages)
        for stage in order:
            args.build_order_file.write(" ".join(stage) + "\n")
    if args.build_srpm:
        srpm_builder = SrpmBuilder()
        for chroot in args.chroot:
            for pkg in list(packages.values()):
                srpm_builder.build_spec(chroot, pkg.spec)
    if args.build:
        assert args.copr_owner, "You need to provide a COPR owner"
        assert args.copr_project, "You need to provide a COPR user"
        assert args.chroot, "You need to provide a chroot to use for builds."
        copr_builder = CoprBuilder(
            copr_owner=args.copr_owner, copr_project=args.copr_project
        )
        success = True
        for chroot in args.chroot:
            tree = Tree(list(packages.values()))
            success &= copr_builder.build_tree(chroot, tree, only_new=args.only_new)
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
