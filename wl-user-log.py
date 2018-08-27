#!/usr/bin/env python


user = raw_input("")
line = raw_input()
lines = []
while line != "end":
   lines.append(line)
   line = raw_input()
i= 0 
while i < len(lines):
   tokens = lines[i].split()
   if tokens[1] == user:
      print lines[i]


   i = i + 1