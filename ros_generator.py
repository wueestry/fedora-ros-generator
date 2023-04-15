import argparse
import os
import subprocess
import sys

from utils.spec_generator import SpecFileGenerator


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Spec files for ROS packages with the " "rosinstall_generator."
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default=False,
        help="Also generate Spec files for dependencies",
    )
    parser.add_argument("--distro", default="noetic", help="The ROS distro (default: %(default)s)")
    parser.add_argument(
        "-t",
        "--template",
        default="templates/pkg.spec.j2",
        help="Path to the Jinja template for the Spec file",
    )
    parser.add_argument(
        "--user_string", default="", help="The user string to use for the changelog"
    )
    parser.add_argument(
        "--bump-release",
        default=False,
        action="store_true",
        help="If set to true, bump the Release: tag by 1",
    )
    parser.add_argument(
        "--release-version", default="", help="The Release: of the resulting Spec files"
    )
    parser.add_argument(
        "-d",
        "--destination",
        default="./specs",
        help="Write generated Spec files to this directory",
    )
    parser.add_argument(
        "-c", "--changelog", type=str, default="", help="The new changelog entry line"
    )
    build_args = parser.add_argument_group("build arguments")
    build_args.add_argument(
        "-b", "--build", action="store_true", default=False, help="Build the generated SPEC file"
    )
    build_args.add_argument(
        "--build-srpm", action="store_true", default=False, help="Generate a SRPM"
    )
    build_args.add_argument(
        "--copr-owner", type=str, help="The owner of the COPR project to use for builds"
    )
    build_args.add_argument("--copr-project", type=str, help="The COPR project to use for builds")
    build_args.add_argument(
        "--chroot",
        action="append",
        type=str,
        help="The chroot used for building the packages, "
        "specify multiple chroots by using the flag "
        "multiple times",
    )
    parser.add_argument(
        "-B",
        "--build-order-file",
        type=argparse.FileType("w"),
        default=None,
        help="Print the order in which the packages should be " "built, requires -r",
    )
    parser.add_argument(
        "--only-new", action="store_true", help="Only build packages that are not in the repo yet"
    )
    parser.add_argument(
        "--no-obsolete-distro-pkg",
        dest="obsolete_distro_pkg",
        action="store_false",
        help="Do not obsolete distro-specific package, e.g., ros-kinetic-catkin",
    )
    parser.add_argument("ros_pkg", nargs="+", help="ROS package name")
    args = parser.parse_args()
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


if __name__ == "__main__":
    main()
