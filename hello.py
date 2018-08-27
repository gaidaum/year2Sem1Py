#!/usr/bin/env python
import sys 

n = sys.argv[1]

print n 

import sys
line = sys.stdin.readlines()
n = int(sys.argv[1])

i = 0 
while i != len(line) and i !=n :
	if len(line) > n :
	   print line[len(line)-n + i].rstrip()

else : 
	print line[i].rstrip
	i = i + 1
