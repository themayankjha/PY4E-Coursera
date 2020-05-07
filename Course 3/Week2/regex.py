#!/usr/bin/python3
import re
filename=input("Enter FileName ")
if len(filename)<1 : filename="regex_sum_42.txt"
file=open(filename)
result=0
for line in file:
    for number in re.findall('[0-9]+',line) :
        result=result+int(number)
print(result)
