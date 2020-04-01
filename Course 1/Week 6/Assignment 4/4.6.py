#!/usr/bin/python3
def computepay(h,r):
    if h>40:
        overtime=h-40
        pay=(40*r)+(overtime*1.5*r)
    else:
        pay=h*r
    return pay
hours=input("Enter hours: ")
rate=input("Enter Rate: ")
h=float(hours)
r=float(rate)
print("Pay",computepay(h,r))
