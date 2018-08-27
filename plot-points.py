#!/usr/bin/env python
import sys 

n = 20

points = {} 
lines = sys.stdin.readlines()

i = 0 
while i < len(lines):
	tokens = lines[i].split()
	key = tokens[0] + "-" + tokens[1]
	points[key] = True
	i = i + 1 

#Header.
print " " + "-" * n

j = 0 
while j < n:
	y = n - j - 1 
	s = ""
	x = 0 
	while x < n:
		key = str(x) + "-" + str(y)
		if key in points:
			s = s + "*"
		else: 
			s = s + " "
		x = x + 1
	print "|" + s + "|"
	j = j + 1
#Footer.
print " " + "-" * n
