#!/usr/bin/env python


import sys 

with open("translation.txt") as f:
	words = f.read().split()


d = {}

i = 0 
while i < len(words)/2:
	d[words[2*i]] = words[2*i+1]
	i += 1

a = sys.stdin.read().split()

i = 0 
while i < len(a):
	if a[i] in d:
		print d[a[i]]

	i +=1