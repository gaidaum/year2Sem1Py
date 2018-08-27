#!/usr/bin/env python


line = raw_input()
lines = []
while line != "end":
   lines.append(line)
   line = raw_input()
i= 0 
while i < len(lines):
   tokens = lines[i].split()
   if int(tokens[2]) >= 7500:
      print lines[i]


   i = i + 1