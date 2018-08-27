#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

numbers = {
	"one": "eins",
	"two": "zwei",
	"three": "drei",
	"four": "view",
	"five": "funf",
	"six": "sechs",
	"seven": "sieben",
	"eight": "acht",
	"nine": "neun",
	"ten": "zehn",
}

i = 0 
while i< len(lines):
	print numbers[lines[i].strip()]
	i = i + 1 