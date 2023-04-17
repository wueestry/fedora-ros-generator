def get_build_order(packages: dict) -> list:
    """Get the order in which to build the given dictionary of packages.
    Each key is a ROS package name, each value is the set of RosPkgs."""
    order = []
    resolved_pkgs = set()
    while resolved_pkgs != set(packages.keys()):
        leaves = set()
        for pkg_name, pkg in packages.items():
            if pkg_name in resolved_pkgs:
                continue
            remaining_deps = set(pkg.get_ros_dependencies()) - resolved_pkgs
            if not remaining_deps.intersection(packages.keys()):
                # No remaining dependencies that are pending to be built.
                # We can build this package.
                leaves.add(pkg_name)
        assert leaves, "No dependency leaves found, cyclic dependencies?"
        order.append(leaves)
        resolved_pkgs |= leaves
    return order
