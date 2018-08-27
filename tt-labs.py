#!/usr/bin/env python

timetable = []

line = raw_input()
while line != "end":
	timetable.append(line)
	line = raw_input()

i = 0 
while i < len(timetable):
	tokens = timetable[i].split()
	if tokens[2] != "1":
		print " ".join(tokens[0:])
	i = i + 1




