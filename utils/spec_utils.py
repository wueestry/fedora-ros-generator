import re


def get_changelog_from_spec(spec: str) -> str:
    """Get the changelog of an existing Spec file.

    Args:
        spec: The path to the Spec file.
    Returns:
        The changelog in the Spec file as string, excluding the %changelog tag.
    """
    spec_as_list = open(spec, "r").readlines()
    return "".join(spec_as_list[spec_as_list.index("%changelog\n") + 1 :])


def get_version_from_spec(spec: str) -> str:
    """Get the version and release from a Spec file.

    Args:
        spec: the path to the Spec file
    Returns:
        A dictionary with keys 'version' and 'release'
    """
    version_info = {}
    for line in open(spec, "r").readlines():
        version_match = re.match("^Version:\s+([\w\.]+)", line)
        if version_match:
            version_info["version"] = version_match.group(1)
            continue
        release_match = re.match("Release:\s+([\w\.]+)(%\{\?dist\})?", line)
        if release_match:
            version_info["release"] = release_match.group(1)
    assert "version" in version_info, "Could not find a Version: tag"
    assert "release" in version_info, "Could not find a Release: tag"
    return version_info
