#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
d = {
   
}

i = 0 
while i < len(s):
   tokens = s[i].split("/")
   token = int(tokens[1])
   if token not in d:
      d[token] = 0
   d[token] = d[token] + 1

   i = i + 1
for token in d:
   print token, d[token]


import sys
lines = sys.stdin.readlines()
a = []
for i in lines:
   i = i.strip()      
   i = i.split('/')       
   if i[1][0] == '0':    
      i[1] = i[1][1]     
   else:
      i[1]               
   a.append(i[1])        

l = []
for i in a:
   if i not in l:      
      l.append(i)
for i in l:
   print ('{}{}{}'.format(i,' ',a.count(i)))