#!/usr/bin/env python

import sys 

i = 0 
count = 0 
n = sys.argv[1:]

while i < len(n):
	if int[n[i]]%2== 1:
		count = count + 1 

	i = i + 1 

	print count




import sys

s = sys.stdin.readlines()
n = int(s[0])

i = 0 
while i <len(s):
	if int[s[i]] < n:
		n = int(s[i])

	i = i + 1 
print n 


#print out names that are born before 1950(oldfucks)


import sys 
n = sys.stdin.readlines()

i = 0 

while i < len(n):
	tokens = n[i].split("/")
	tokens = tokens[2].split()
	if tokens[0] < "50":
		print " ".join(tokens[2:])

	i = i + 1

#search for the count of non-empty strings in a list

i = 0 
total = 0 
while i <len(a):
	if a[i] != "":
		total = total + 1
	i = i + 1 
print total 





#linear search for the first non-empty string

i = 0 

while i <len(a) and a[i] == "":
	i = i + 1 

if i < len(a):
	print a[i]

#search for words and only output if its 6 or more characters

i = 0 
while i <len(a):
	if len(a[i]) >=6:
			print a[i]

	i = i + 1
 

 #Linear search print the first word thats 6 or more characters

 i = 0 
 while i <len(a) and len(a[i]) <6:
 	i = i + 1

 if i<len(a):
 	print a[i]



#prefix1 

i = 0 

while i < len(a):
	if a[i][:len(s)] == s:
			print a[i]

	i = i + 1 


#prefix 2

i = 0 
while i <len(a) and not a[i][:len(s)] == s:
	i = i + 1 

if i < len(a):
	print a[i]

#prime 1

i = 0 
while i <len(a):
	if isprime(a[i]):
		print a[i]

	i = i + 1


#prime 2 linear search 

i = 0 
while i < len(a) and not isprime(a[i]):
	i = i + 1

if i <len(a):
	print a[i]

#if a list a contains a string s or not

i = 0 
while i < len(a):
	if len(s)== len(a) and s[i] == a[i]:
		print True

	else:
		print False

	i = i + 1




#remove the duplicate words from a list


import sys 
seen = []

line = sys.stdin.readline()

while 0 < len(line):
	i = 0 
	while i < len(seen) and seen[i] != line:
		i = i + 1

	if i == len(seen):
		print line.rstrip()
		seen.append(line)

	line = sys.stdin.readline()


#potpourri reverse lines

def reverse(string):
	results = string[::-1]
	return string[::-1]




#filenames

import sys 
lines = sys.stdin.readlines()

i = 0 
while i < len(lines):
	tokens = lines[i].rstrip().split("/")
	parse = tokens[-1].split(".")

	print tokens[-1]

	i = i + 1 

#filenames


import sys 
pattern = sys.argv[1]

lines = sys.stdin.readlines()

i = 0 

while i < len(lines):
	tokens = lines[i].rstrip().split("/")
	parse = tokens[-1].split(".")
	if parse [1] == pattern:
		print tokens[-1]

	i = i + 1 


#write hello from a text 

with open ("hello.txt",w) as f:
	f.write("Hello world.\n")

#read file 


import sys 
with open ("input.txt") as f:
	sys.stdout.write(f.read())


# sum from file 1


import sys 
with open("numbers.txt") as f:
	count = 0 
	num = f.readline()
	while len(num) != 0 :
		count = count + int(num)
		num = f.readline()

sys.stdout.write(str(count) + "\n")


#sumfromfile-2

import sys 
x = sys.argv[1]
with open(x) as f:
	count = 0 
	num = f.readline()
	while len(num) != 0 ; 
		count = count + int(num)
		num = f.readline()

sys.stdout.write(str(count) + "\n")

#sumfromfile-3

import sys 
filename= sys.argv[1]

with open(filename) as f:
	tokens = f.read().split()

total = 0 

while len(filename) != 0:
	total = total + int(tokens)
	tokens = f.read().split()

sys.stduout.write(int(total) + "\n")


#grep1

import sys 
pattern = sys.argv[1]
filename = sys.argv[2]

with open (filename) as f:
	a = f.readlines()

i = 0 
while i <len(a):
	s = a[i]

	j = 0 
	while j < len(s) and s[j:k+len(pattern)] != pattern:
		j = j + 1
	if j <len(s):
		print s.rstrip()
	i = i + 1


#GREP2

import sys 
pattern = sys.argv[1]
filename = sys.argv[2]
count = 0 
while count != len(filename):
	with open(filename[count]) as f:
		a = f.readlines()

	i = 0 
	while i < len(a):
		s = a[i]

		j = 0 
		while j < len(s) and s[j:j + len(pattern)] != pattern:
			j = j + 1 

		if j < len(s):
			print s.rstrip()

		i = i + 1
	count = count + 1


# Dictionary tasks print out only fruit 


import sys 
lines = sys.stdin.readlines()

fruit = {
	"apple": True,
	"pair": True,
	"orange": True,
	"banana": True,
	"cheery": True,	
}

i = 0 
while i < len(lines):
	word = lines[i].rstrip()
	if word in fruit 
		sys.stdout.write(lines[i])

	i = i + 1 


#Dictionary of German to English 

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
while i < len(lines):
	print numbers[lines[i].strip()]
	i = i + 1



#Word translation 


import sys 
with open("translation.txt") as f:
	words = f.read().split()


d = {}

i = 0 
while i < len(words)/2:
	d[words[2*i]] = words[2*i+1]
	i += 1

a = sys.stdin.read().split()

i = 0 
while i < len(a):
	if a[i] in d:
		print d[a[i]]

	i += 1