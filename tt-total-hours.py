#!/usr/bin/env python
 
line = raw_input()

numbers = 0

while line != "end":
   numbers = numbers + int(line[5])
   line = raw_input()
print (numbers)