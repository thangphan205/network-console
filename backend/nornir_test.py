from nornir import InitNornir
from settings import settings
import pynetbox
from pprint import pprint

nr = InitNornir(inventory=settings.INVENTORY_SWITCH)

devices = []
for i in nr.inventory.hosts:
    device = {}
    for j in nr.inventory.hosts[i].keys():
        device[j] = nr.inventory.hosts[i][j]
    devices.append(device)

pprint(devices)

"""
[{'asset_tag': None,
  'cluster': None,
  'comments': '',
  'config_context': {},
  'created': '2020-10-18',
  'custom_fields': {},
  'device_role': {'id': 1,
                  'name': 'Access Switch',
                  'slug': 'access-switch',
                  'url': 'http://netbox.hocmang.net/api/dcim/device-roles/1/'},
  'device_type': {'display_name': 'Cisco C2960',
                  'id': 1,
                  'manufacturer': {'id': 1,
                                   'name': 'Cisco',
                                   'slug': 'cisco',
                                   'url': 'http://netbox.hocmang.net/api/dcim/manufacturers/1/'},
                  'model': 'C2960',
                  'slug': 'c2960',
                  'url': 'http://netbox.hocmang.net/api/dcim/device-types/1/'},
  'display_name': 'C2960_1',
  'face': None,
  'id': 1,
  'last_updated': '2020-10-24T15:28:17.698493Z',
  'local_context_data': None,
  'name': 'C2960_1',
  'parent_device': None,
  'platform': {'id': 1,
               'name': 'IOS',
               'slug': 'ios',
               'url': 'http://netbox.hocmang.net/api/dcim/platforms/1/'},
  'position': None,
  'primary_ip': {'address': '192.168.4.1/24',
                 'family': 4,
                 'id': 2,
                 'url': 'http://netbox.hocmang.net/api/ipam/ip-addresses/2/'},
  'primary_ip4': {'address': '192.168.4.1/24',
                  'family': 4,
                  'id': 2,
                  'url': 'http://netbox.hocmang.net/api/ipam/ip-addresses/2/'},
  'primary_ip6': None,
  'rack': None,
  'serial': '',
  'site': {'id': 1,
           'name': 'Ho Chi Minh',
           'slug': 'ho-chi-minh',
           'url': 'http://netbox.hocmang.net/api/dcim/sites/1/'},
  'status': {'label': 'Active', 'value': 'active'},
  'tags': [],
  'tenant': None,
  'url': 'http://netbox.hocmang.net/api/dcim/devices/1/',
  'vc_position': None,
  'vc_priority': None,
  'virtual_chassis': None}]
"""