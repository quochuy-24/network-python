# -*- coding: utf-8 -*-
"""
Task 4.6

Process the ospf_route string and print the information to the stdout as follows:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

parts = ospf_route.split()
clean_parts = [part.strip(',[]') for part in parts]

prefix = clean_parts[0]
ad_metric = clean_parts[1]
next_hop = clean_parts[3]
last_update = clean_parts[4]
outbound_interface = clean_parts[5]
table = f"""
{"Prefix":<22}{prefix}
{"AD/Metric":<22}{ad_metric}
{"Next-Hop":<22}{next_hop}
{"Last update":<22}{last_update}
{"Outbound Interface":<22}{outbound_interface}
"""
print(table)
