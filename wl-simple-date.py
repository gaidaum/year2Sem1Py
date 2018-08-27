
#!/usr/bin/env python


line = raw_input()
lines = []
while line != "end":
   lines.append(line)
   line = raw_input()
i= 0 
while i < len(lines):
   parse = lines[i].split()
 
   print lines

   i = i + 1