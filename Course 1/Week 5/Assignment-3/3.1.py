#!/usr/bin/python3
hours=input("Hours? ")
rate=input("Rate? ")
if float(hours)>40:
    overtime=float(hours)-40
    payout=(float(overtime)*1.5*float(rate))+(40*float(rate))
else :
    payout=(float(hours)*float(rate))
print(payout)
