import os
import subprocess

import dnf


class PkgResolver:
    def __init__(self) -> None:
        base = dnf.Base()
        base.read_all_repos()
        base.fill_sack()
        q = base.sack.query()
        self.available_pkgs = q.available()

    def get_system_package_name(self, pkg_name: str, rosdistro: str) -> list:
        env = os.environ.copy()
        env["ROS_DISTRO"] = rosdistro
        cmd = subprocess.run(
            ["rosdep", "--rosdistro={}".format(rosdistro), "resolve", pkg_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        deps = []
        if cmd.returncode == 0:
            lines = cmd.stdout.decode().split("\n")
            deps = [dep for dep in lines if not (dep == "" or dep == "#dnf")]
        else:
            res = self.available_pkgs.filter(name=pkg_name)
            deps = set([pkg.name for pkg in res])
            assert len(deps) > 0, "Could not find system package {}: {}".format(
                pkg_name, cmd.stderr.decode().rstrip() or cmd.stdout.decode().rstrip()
            )
        assert len(deps) == 1, "Expected exactly one name, got: {}".format(deps)
        return deps.pop()
