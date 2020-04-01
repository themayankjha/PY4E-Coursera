#!/usr/bin/python3
largest=None
smallest=None
while True:
    num=input("Number?: ")
    if num == "done":
        print("Maximum is",largest)
        print("Minimum is",smallest)
        break;
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest=num
    if smallest is None:
        smallest=num
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
