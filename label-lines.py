#!/usr/bin/env python


n = raw_input()

a = []

while n != "end":
	a.append(n)
	n = raw_input()

i = 0 
while i < len(a):
   print i, len(a), a[i]
   i = i + 1