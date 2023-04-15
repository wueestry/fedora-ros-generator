import dnf


class PkgResolver:
    def __init__(self) -> None:
        base = dnf.Base()
        base.read_all_repos()
        base.fill_sack()
        q = base.sack.query()
        self.available_pkgs = q.available()
