#!/usr/bin/env python

import sys

seen = []

line = sys.stdin.readline()
while 0 < len(line):
	i = 0 
	while i < len(seen) and seen[i] != line:
		i = i + 1

	if i == len(seen):
		print line.rstrip()
		seen.append(line)

	line = sys.stdin.readline()