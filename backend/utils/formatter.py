import re


def is_valid_mac(mac_addr: str) -> bool:
    """Check if a given MAC address is valid."""
    if (
        re.search(r"^\s*(?:[0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}\s*$", mac_addr) is not None
        or re.search(r"^\s*(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\s*$", mac_addr) is not None
        or re.search(r"^\s*(?:[0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2}\s*$", mac_addr) is not None
        or re.search(r"^\s*[0-9a-fA-F]{6}-[0-9a-fA-F]{6}\s*$", mac_addr) is not None
    ):
        return True
    return False


def convert_mac(mac_addr: str) -> str:
    """Convert MAC address format to xx:xx:xx:xx:xx:xx"""
    mac_addr = mac_addr.strip()
    if ":" in mac_addr:
        return mac_addr.lower()
    elif "." in mac_addr:
        no_splitter_mac = "".join(mac_addr.split(".")).lower()
    elif "-" in mac_addr:
        no_splitter_mac = "".join(mac_addr.split("-")).lower()
    else:
        raise ValueError("Unknown MAC address format.")
    return ":".join([no_splitter_mac[i : i + 2] for i in range(0, len(no_splitter_mac), 2)])


def standardize_interface(intf: str) -> str:
    """Standardize interface format to Fax/x or Gix/x.

    For instance: FastEthernet0/0 -> Fa0/0
                  GigabitEthernet4/5 -> Gi4/5
    """
    if "Port-channel" in intf:
        return f"Po{intf.split('channel')[1]}"

    slash_index = intf.find("/")
    if "Fast" in intf:
        return f"Fa{intf[slash_index-1 : ]}"
    elif "Gigabit" in intf:
        return f"Gi{intf[slash_index-1 : ]}"
    else:
        raise ValueError("Unexpected interface format.")
