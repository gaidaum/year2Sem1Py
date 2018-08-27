#!/usr/bin/env python
line = raw_input()
lines = []
while line != "end":
   lines.append(line)
   line = raw_input()

n = input()

for l in lines:
   if int(l[0]) == n:
      print (l)