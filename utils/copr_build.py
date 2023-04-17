import argparse

from utils import spec_utils
from utils.copr_builder import CoprBuilder


class CoprBuildError(Exception):
    def __init__(self, error: object) -> None:
        self.error = error

    def __str__(self) -> str:
        return repr(self.error)


def main() -> None:
    """Main function to directly build a SPEC file."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        default=False,
        help="Force a rebuild if package was already built",
    )
    parser.add_argument(
        "--copr-owner", type=str, help="The owner of the COPR project to use for builds"
    )
    parser.add_argument("--copr-project", type=str, help="The COPR project to use for builds")
    parser.add_argument("--chroot", action="append", help="The chroot(s) to use for the packages")
    parser.add_argument(
        "--spec-dir", default="./specs/", help="The directory where to look for SPEC files"
    )
    parser.add_argument("pkg_name", nargs="+")
    args = parser.parse_args()
    copr_builder = CoprBuilder(args.copr_owner, args.copr_project)
    for chroot in args.chroot:
        for pkg in args.pkg_name:
            spec = args.spec_dir + pkg + ".spec"
            need_build = args.force
            if not need_build:
                version_info = spec_utils.get_version_from_spec(spec)
                ver_rel = f'{version_info["version"]}-{version_info["release"]}'
                need_build = not copr_builder.pkg_is_built(chroot, pkg, ver_rel)
            if need_build:
                copr_builder.build_spec(chroot=chroot, spec=spec, wait_for_completion=True)


if __name__ == "__main__":
    main()
