#!/usr/bin/env python

import sys 


lines = sys.stdin.readlines()

i = 0 
while i < len(lines):
	tokens = lines[i].rstrip().split("/")
	parse = tokens[-1].split(".")
	
	print tokens[-1]

	i = i + 1 
