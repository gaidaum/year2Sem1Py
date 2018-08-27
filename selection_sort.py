#!/usr/bin/env python

def swap(a , i, j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp

def find_position_of_smallest(a,i):
 	n = i
 	i = i + 1
	while i < len(a):
 		if a[i] < a[n]:
 			n = i 
		i = i + 1
 	return n

def sort(a):
 	
	i = 0 
	while i < len(a):
		p = i 
		j = i + 1 
		while j < len(a):
			if a [j] < a [p]:
				p = j 
			j = j + 1 

		tmp = a[p]	
		a[p] = a[i]
 		a[i] = tmp

		i = i + 1