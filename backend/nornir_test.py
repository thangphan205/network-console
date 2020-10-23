from nornir import InitNornir
from settings import settings
import pynetbox

nr = InitNornir(
    inventory={
        "plugin": "NetBoxInventory2",
        "options": {
            "nb_url": "http://netbox.hocmang.net",
            "nb_token": "e91d18faac0d56516c81cd9fd384a80d118c3238",
        },
    }
)
print(nr.inventory.hosts)
print(nr.inventory.groups)