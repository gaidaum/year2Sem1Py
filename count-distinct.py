#!/usr/bin/env python

n = input()
a = [] 
while n != "0":
   a.append(n)
   n = input()

count = 0
x = []

for l in a:
   if l not in x:
      x.append(l)
      count+=1

print (count)