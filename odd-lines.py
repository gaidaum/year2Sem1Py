#!/usr/bin/env python
import sys

n = sys.stdin.readlines()
i = 0 

for i in n :
  i = i.strip()
  if  int(i)%2== 1: 
     print i 



