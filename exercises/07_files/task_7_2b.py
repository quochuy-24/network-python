# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
import sys
ignore = ["duplex", "alias", "configuration"]

file_name = sys.argv[1]
result_file = sys.argv[2]

with open(file_name, 'r') as f, open(result_file,'w') as dest:
  for line in f:
    flag = True
    if line.startswith('!'):
      flag=False
    for word in ignore:
      if word in line:
        flag = False

    if not flag:
      continue
    dest.write(line)
    