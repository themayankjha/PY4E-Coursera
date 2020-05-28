#!/usr/bin/python3
name=input("Enter File: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time=list()
hourcount=dict()
for lines in handle :
    if not lines.startswith("From") : continue
    if lines.startswith("From:") : continue
    time.append(lines.split()[5].split(":")[0])
for hours in time :
    hourcount[hours]=hourcount.get(hours,0)+1
for k,v in sorted(hourcount.items()) :
    print(k,v)
    
