#!/usr/bin/env python

line = raw_input()
lines = []
while line != "end":
   lines.append(line)
   line = raw_input()
i= 0 
while i < len(lines):
	tokens = lines[i].split(":")

	print "".join(tokens[0]), "".join(tokens[6])


	i = i + 1