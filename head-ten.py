#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
o = []

for i in lines : 
	o.append(i)
if len(o) > 10 :
	o = o[0:10]
else : 
	o 
for w in o:
	print w.rstrip()