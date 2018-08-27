#!/usr/bin/env python
import sys

lines = sys.stdin.readlines()
lines = ''.join(lines).split()


a = []
i = 0
while i < len(lines):
   if lines.count(lines[i]) >= 2:
      a.append(lines[i])
   i+=1
if len(a) > 0:
   print 'snap:' + ' ' + a[0]
else:
   a