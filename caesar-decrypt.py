#!/usr/bin/env python
import sys
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

source = lower + upper 
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

d = {}

i = 0 
while i < len(source):
	d[source[i]] = dst[i]
	i = i + 1
import sys
message = sys.stdin.read()
s = ""
i = 0 
while i < len(message):
	if message[i] in d:
		s = s + d[message[i]]
	else:
		s = s + message[i]
	i = i + 1

sys.stdout.write(s)