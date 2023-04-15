import queue
import threading
from typing import List

import jinja2

from utils.package_resolver import PkgResolver


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
        self.generated_packages = {}
        self.packages_lock = threading.Lock()
