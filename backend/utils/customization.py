from nornir.core import Nornir
from nornir.core.inventory import ConnectionOptions


def reset_conn_options(nr: Nornir) -> None:
    """Remove all connection options for hosts contained in a Nornir object.

    Args:
        nr: a Nornir object.
    """
    for host in nr.inventory.hosts.values():
        host.connection_options = {}


def disable_fast_cli(nr: Nornir) -> None:
    """
    Disable `fast_cli` option in netmiko. This option is only appropriate
    for Cisco IOS devices.

    Args:
        nr: a Nornir object.
    """
    conn_options = ConnectionOptions(extras={"fast_cli": False})
    for host in nr.inventory.hosts.values():
        if host.platform == "ios":
            host.connection_options["netmiko"] = conn_options


def enable_fast_cli(nr: Nornir) -> None:
    """
    Enable `fast_cli` option in netmiko. This option is only appropriate
    for Cisco IOS devices.

    Args:
        nr: a Nornir object.
    """
    conn_options = ConnectionOptions(extras={"fast_cli": True})
    for host in nr.inventory.hosts.values():
        if host.platform == "ios":
            host.connection_options["netmiko"] = conn_options
