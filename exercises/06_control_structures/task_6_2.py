# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip_add = input()
first_byte = ip_add.split('.')[0]
if int(first_byte) >= 1 and int(first_byte) <= 223:
  print('unicast')
elif int(first_byte) >= 224 and int(first_byte) <= 239:
  print('multicast')
elif ip_add == '0.0.0.0':
  print('unassigned')
elif ip_add == '255.255.255.255':
  print('local broadcast')
else:
  print('unused')