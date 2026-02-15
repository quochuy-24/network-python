# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
#O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
template = (
  'Prefix                {}\n'
  'AD/Metric             {}\n'
  'Next-Hop              {}\n'
  'Last update           {}\n'
  'Outbound Interface    {}'
)

with open('ospf.txt','r') as f:
  for line in f:
    new_line = line.replace('[', '').replace(']', '').replace(',', '')
    _, prefix, ad_metric, _, next_hop, last_update, outbound_interface = new_line.split()
    print(template.format(prefix,ad_metric,next_hop,last_update, outbound_interface))
    
