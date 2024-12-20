"""Caracara meta class.

Returns information about Caracara itself, such as its package version and
a custom user agent string based on Caracara's version.
"""

import importlib.metadata

_pkg_version = importlib.metadata.version("caracara")


def user_agent_string():
    """
    Return the default Caracara user agent.

    This user agent will be sent to CrowdStrike with API requests, including Caracara's version,
    unless the developer overrides this when instantiating a Client object.
    """
    return f"crowdstrike-caracara/{_pkg_version}"
