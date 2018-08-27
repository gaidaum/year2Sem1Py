#!/usr/bin/env python
s = raw_input()

output = []
while s != "end":
	output.append(s)
	s = raw_input()


i = 0
while i < len(output):
	print output[-i - 1]
	i = i + 1
