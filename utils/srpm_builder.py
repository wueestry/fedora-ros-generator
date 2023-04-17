import os
import re
import subprocess


class SrpmBuilder:
    def build_spec(self, chroot: str, spec: str) -> str:
        """Build a SPEC file into a SRPM

        Args:
            chroot: The chroot to use for the build, e.g., fedora-26-x86_64
            spec: The path to the SPEC file of the package.
            wait_for_completion: If set to true, wait for the build to finish
        """
        print(f"Building {spec} for chroot {chroot}")
        res = subprocess.run(
            ["spectool", "-g", spec, "-C", os.path.expanduser("~/rpmbuild/SOURCES")],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
        assert res.returncode == 0, "Failed to fetch sources for " + spec
        res = subprocess.run(
            ["rpmbuild", "-bs", spec], universal_newlines=True, stdout=subprocess.PIPE
        )
        assert res.returncode == 0, "Failed to build SRPM for " + spec
        match = re.search("Wrote: (\S+)", res.stdout)
        assert match, f"Unexpected output from rpmbuild: {res.stdout}"
        srpm = match.group(1)
        return srpm
