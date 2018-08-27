#!/usr/bin/env python

timetable = []

line = raw_input()
while line != "end":
   timetable.append(line)
   line = raw_input()

i = 0
while i < len(timetable):
   parse = timetable[i].split()
   print parse[3]
 
   i = i + 1