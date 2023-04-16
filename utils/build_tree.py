
import pygraphviz as pgv
from utils.build_node import Node
from utils.build_state import BuildState

class Tree:
    def __init__(self, pkgs):
        self.nodes = {}
        for pkg in pkgs:
            self.add_pkg(pkg)
        assert len([n for n in self.nodes.values() if n.is_initialized()]) == len(pkgs), f'Unexpected number of nodes: {len(self.nodes)}, ' 'expected: {len(pkgs)}'
        for node in self.nodes.values():
            if not node.is_initialized():
                node.state = BuildState.SKIPPED

    def add_pkg_stub(self, pkg_name):
        """ Add a node that only contains the name to the tree.

        Returns:
            The newly created node if not yet in the tree or the tree node if
            already exists.
        """
        if pkg_name in self.nodes:
            return self.nodes[pkg_name]
        else:
            node = Node(pkg_name)
            self.nodes[pkg_name] = node
            return node

    def add_pkg(self, pkg):
        if not pkg.name in self.nodes:
            node = Node(pkg.name)
            node.pkg = pkg
            self.nodes[pkg.name] = node
        else:
            node = self.nodes[pkg.name]
        if not node.is_initialized():
            deps = []
            for dep in pkg.get_build_dependencies()['ros'] | \
                       pkg.get_run_dependencies()['ros']:
                deps.append(self.add_pkg_stub(dep))
            node.init_deps(deps)
            node.pkg = pkg

    def get_build_leaves(self):
        """Return all nodes that have no unbuilt dependencies."""
        leaves = []
        for node in self.nodes.values():
            if not node.state == BuildState.PENDING:
                continue
            is_leave = True
            for dep in node.dependencies:
                if not dep.state in [BuildState.SUCCEEDED, BuildState.SKIPPED]:
                    is_leave = False
            if is_leave:
                leaves.append(node)
        return leaves

    def is_built(self):
        """ Check if all packages have been built successfully. """
        for node in self.nodes.values():
            if not node.state in [BuildState.SUCCEEDED, BuildState.SKIPPED]:
                return False
        return True

    def is_failed(self):
        """ Check if any build and therefore the build tree failed. """
        for node in self.nodes.values():
            if node.state == BuildState.FAILED:
                return True
        return False

    def get_build_progress(self):
        """ Count the number of finished and failed builds in the tree."""
        building = 0
        finished = 0
        failed = 0
        for node in self.nodes.values():
            if node.state == BuildState.BUILDING:
                building += 1
            elif node.state in [BuildState.SUCCEEDED, BuildState.SKIPPED]:
                finished += 1
            elif node.state == BuildState.FAILED:
                failed += 1
        return {
            'building': building,
            'finished': finished,
            'failed': failed,
            'total': len(self.nodes)
        }

    def to_dot(self):
        """ Generate a DOT representation of the tree.

        Returns:
            A pgv graph object.
        """
        graph = pgv.AGraph(directed=True)
        graph.node_attr['shape'] = 'rectangle'
        for node in self.nodes:
            graph.add_node(node)
        for node in self.nodes.values():
            for dep in node.dependencies:
                graph.add_edge(node.name, dep.name)
        return graph

    def draw_tree(self, output_file):
        graph = self.to_dot()
        graph.draw(output_file, prog='dot')