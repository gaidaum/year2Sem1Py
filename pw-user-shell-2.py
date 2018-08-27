#!/usr/bin/env python

line = raw_input()
lines = []

while line != "end":
   lines.append(line)
   line = raw_input()

i= 0 
while i < len(lines):
	tokens = lines[i].split(":")
	if tokens[6] != "/bin/false" and tokens[6] != "/usr/sbin/nologin":

		print tokens[0], tokens[6]


	i = i + 1