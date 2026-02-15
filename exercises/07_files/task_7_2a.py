# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
import sys
ignore = ["duplex", "alias", "configuration"]


file_name = sys.argv[1]
with open(file_name, 'r') as f:
  for line in f:
    flag = True
    if line.startswith('!'):
      flag=False
    for word in ignore:
      if word in line:
        flag = False

    if not flag:
      continue
    print(line.rstrip())