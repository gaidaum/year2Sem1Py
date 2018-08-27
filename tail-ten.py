#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

i = 0 
while i < len(lines):
   if len(lines) - i <= 10:
      print lines[i].rstrip()
   i = i + 1
