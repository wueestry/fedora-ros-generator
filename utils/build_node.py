from typing import List, Optional

from utils.build_state import BuildState
from utils.ros_package import RosPkg


class Node:
    def __init__(self, name: str, pkg: Optional[RosPkg] = None) -> None:
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

    def init_deps(self, deps: List["Node"]):
        """Initialize the dependencies of the node.

        This must happen in a separate step because the dependencies may not yet
        be in the tree during the creation of this object.

        Args:
            deps: A list of strings of package name this package depends on.
        """
        self.dependencies = deps

    def is_initialized(self) -> bool:
        return self.pkg != None and self.dependencies != None

    def is_built(self) -> bool:
        return self.built
