# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

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