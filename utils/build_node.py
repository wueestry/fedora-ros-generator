from utils.build_state import BuildState

class Node:
    def __init__(self, name, pkg=None):
        """Fully initialize the note.

        Args:
            name: The package name, e.g., ros-kinetic-catkin
            pkg: The name of this package.
        """
        self.name = name
        self.state = BuildState.PENDING
        self.build_id = None
        self.initialized = False
        self.pkg = pkg
        self.dependencies = None

    def init_deps(self, deps):
        """ Initialize the dependencies of the node.

        This must happen in a separate step because the dependencies may not yet
        be in the tree during the creation of this object.

        Args:
            deps: A list of strings of package name this package depends on.
        """
        self.dependencies = deps

    def is_initialized(self):
        return self.pkg != None and self.dependencies != None

    def is_built(self):
        return self.built