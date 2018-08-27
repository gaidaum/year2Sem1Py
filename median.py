#!/usr/bin/env python

import selection_sort

n = input()

numbers = []

while n != 0:
	numbers.append(n)
	n = input()
selection_sort.sort(numbers)

print (numbers[len(numbers)/2])