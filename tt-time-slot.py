#!/usr/bin/env python

line = raw_input()

a = []
while line != "end":
   
   if int(line[5]) == 1:
      a.append(line[0:2]+line[2:4]+":00"+ " "+line[2:4]+":50"+" "+line[7:])
   else: 
      a.append(line[0:4]+":00"+" "+"{}{}".format(int(line[5]) + int(line[2:4])-1,":50")+" "+line[7:])
   line = raw_input()
   
for i in a:
   if  int(i[2:4]) < 10:
      print (i[0:1]+" "+i[3:7]+" "+i[9:])
   else:
      print (i)