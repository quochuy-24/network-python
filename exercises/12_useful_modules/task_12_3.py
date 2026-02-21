# -*- coding: utf-8 -*-
"""
Task 12.3

Create a function print_ip_table that prints a table of available
and unavailable IP addresses.

The function expects two lists as arguments:
* list of available IP addresses
* list of unavailable IP addresses

The result of the function is printing a table to the stdout:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
"""
from task_12_2 import convert_ranges_to_ip_list
from task_12_1 import ping_ip_addresses
from tabulate import tabulate

def print_ip_table(pingable, unpingable):
  data = {
    'Reachable':pingable,
    'Unreachable': unpingable
  }
  print(tabulate(data,headers='keys'))

if __name__=="__main__":
  ip_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
  clean_ip_list = convert_ranges_to_ip_list(ip_list)
  pingable, unpingable = ping_ip_addresses(clean_ip_list)
  print_ip_table(list(pingable),list(unpingable))

