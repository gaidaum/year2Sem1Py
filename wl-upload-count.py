#!/usr/bin/env python

line = raw_input()


count = 0 
lines = []
while line != "end":
  if "POST" in line:
  	count += 1 
  line = raw_input()

print(count)