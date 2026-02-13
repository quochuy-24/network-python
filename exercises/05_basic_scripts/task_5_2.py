# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip_input = input("Ask the user to enter the IP network in the format: ")
network, netmask = ip_input.split('/')
ip_parts = network.split('.')
number_netmask = int(netmask)
netmask_binary = '1' * number_netmask + '0' * (32-number_netmask)
ouput = (
  'Network:\n'
  f'{ip_parts[0]:<10}{ip_parts[1]:<10}{ip_parts[2]:<10}{ip_parts[3]:<10}\n'
  f'{f"{int(ip_parts[0]):08b}":<10}{f"{int(ip_parts[1]):08b}":<10}{f"{int(ip_parts[2]):08b}":<10}{f"{int(ip_parts[3]):08b}":<10}\n\n'
  'Mask:\n'
  f'/{netmask}\n'
  f'{int(netmask_binary[0:8],2):<10}{int(netmask_binary[8:16],2):<10}{int(netmask_binary[16:24],2):<10}{int(netmask_binary[24:32],2):<10}\n'
  f'{netmask_binary[0:8]:<10}{netmask_binary[8:16]:<10}{netmask_binary[16:24]:<10}{netmask_binary[24:32]:<10}'
)
print(ouput)