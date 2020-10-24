from nornir import InitNornir
from settings import settings


class NornirModel:
    """
    Init Nornir Model to communicate with netbox.
    """

    def init_nornir():
        nr = None
        try:
            nr = InitNornir(inventory=settings.INVENTORY_SWITCH)
        except Exception as exc:
            print(exc)
        return nr

    def get_devices():
        nr = NornirModel.init_nornir()
        devices = []
        for i in nr.inventory.hosts:
            device = {}
            for j in nr.inventory.hosts[i].keys():
                device[j] = nr.inventory.hosts[i][j]
            devices.append(device)
        return devices
