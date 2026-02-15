# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
vlan_input = input("Enter VLAN number: ")
f = open('CAM_table.txt','r')
while True:
  line = f.readline()
  if line.startswith('Vlan'):
    line = f.readline()
    break
template = ('{:<9}{:<22}{}')
mac_table = []
for line in f:
  vlan, mac,_, interface = line.split()
  if vlan == vlan_input:
    print(template.format(vlan, mac, interface))
f.close()
