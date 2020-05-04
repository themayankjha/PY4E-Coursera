#!/usr/bin/python3
fname=input("Enter the name of the file")
fh =open(fname)
lst=list()
for line in fh:
    templist=line.split()
    for word in templist:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
