#!/usr/bin/env python
import sys

n = sys.argv[1]
 
lines = sys.stdin.readlines()
lines = lines[0:int(n)]
for i in lines :
	print i.rstrip()