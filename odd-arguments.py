#!/usr/bin/env python

import sys 
i = 0 
n = sys.argv[1:]
while i < len(n):

   if int(n[i])%2 ==1: 
	  print n[i]

   i = i + 1 
