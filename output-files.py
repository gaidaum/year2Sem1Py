#!/usr/bin/env python

import sys 

x = sys.argv[1:]
i = 0 
while i != len(x):
	with open(x[i]) as f:
		a = f.read()
		sys.stdout.write(a)
	i = i + 1
		