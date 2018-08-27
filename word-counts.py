#!/usr/bin/env python
import sys 
s = sys.stdin.readlines()


i = 0 
while i < len(s):
	tokens = s[i].split()

	
	print len(tokens[0:])
	i = i + 1