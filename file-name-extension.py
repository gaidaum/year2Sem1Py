#!/usr/bin/env python

import sys 
pattern = sys.argv[1]

lines = sys.stdin.readlines()

i = 0 
while i < len(lines):
	tokens = lines[i].rstrip().split("/")
	parse = tokens[-1].split(".")
	if parse [1] == pattern:
		print tokens[-1]

	i = i + 1 
