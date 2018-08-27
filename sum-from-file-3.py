#!/usr/bin/env python
import sys
filename = sys.argv[1]

with open(filename) as f:
   rawfile=f.read()
   numbers= rawfile.split()
   total=0
   i=0
   while i != len(numbers):
      total=total + int(numbers[i])
      i=i+1
   print total