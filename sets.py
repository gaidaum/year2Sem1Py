#!/usr/bin/env python

def union(a,b):
	 seen = {}

	 i = 0 
	 while i < len(a):
	 	seen[a[i]] = True
	 	i = i + 1

	 k = 0

	 while k < len(b):
	 	if not (b[k] in seen):
	 		seen[b[k]] = True

	 	k = k + 1

	 return seen 

def intersection(a,b):

	seen = {}

	i = 0
	while i < len(a):
		if a[i] in b and not (a[i] in seen): 
			seen[a[i]] = True

		i = i + 1

	return seen