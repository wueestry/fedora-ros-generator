import enum

class BuildState(enum.Enum):
    PENDING = enum.auto()
    BUILDING = enum.auto()
    FAILED = enum.auto()
    SUCCEEDED = enum.auto()
    ABORTED = enum.auto()
    SKIPPED = enum.auto()