# -*- coding: utf-8 -*-
"""
Task 9.3

Create a get_int_vlan_map function that handles the switch configuration
file and returns a tuple of two dictionaries:

* a dictionary of ports in access mode, where the keys are port numbers,
  and the access VLAN values (numbers):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* a dictionary of ports in trunk mode, where the keys are port numbers,
  and the values are the list of allowed VLANs (list of numbers):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw1.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
def get_int_vlan_map(config_filename):
  access = {}
  trunk = {}
  with open(config_filename,'r') as f:
    for line in f:
      if line.startswith('interface'):
        interface = line.split()[-1].strip()
      elif 'trunk allowed vlan' in line:
        raw_vlans = line.split()[-1].strip()
        vlans = [int(x) for x in raw_vlans.split(',')]
        trunk[interface] = vlans
      elif 'access vlan' in line:
        vlan = int(line.split()[-1].strip())
        access[interface] = vlan
  return access,trunk

print(get_int_vlan_map('config_sw1.txt'))
        