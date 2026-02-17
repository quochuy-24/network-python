# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

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
        elif 'mode access' in line:
            access[interface] = 1
        elif 'access vlan' in line:
            vlan = int(line.split()[-1].strip())
            access[interface]= vlan
  return access,trunk

print(get_int_vlan_map('config_sw2.txt'))