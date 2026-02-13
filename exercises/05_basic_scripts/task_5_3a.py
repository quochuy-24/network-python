# -*- coding: utf-8 -*-
"""
Task 5.3a

Copy and change the script from task 5.3 in such a way that, depending on
the selected mode, different questions were asked in the request for the VLAN number
or VLAN list:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter the allowed VLANs:'

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]


interface_mode = input("Enter interface mode (access/trunk): ")
interface_name = input("Enter interface type and number: ")
result = ""
if interface_mode == 'access':
    vlans = input("Enter VLAN number:")
    result = '\n'.join(access_template)
elif interface_mode == 'trunk':
    vlans = input("Enter the allowed VLANs:")
    result = '\n'.join(trunk_template)
print(f'interface {interface_name}')
print(result.format(vlans))