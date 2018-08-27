#!/usr/bin/env python

timetable = []


line = raw_input()
while line != "end":
   timetable.append(line)
   line = raw_input()

i = 0
while i < len(timetable):
	parse = timetable[i].split()
	if parse[0] == "3":

		print  " ".join(parse[0:])

	
	i = i + 1
  