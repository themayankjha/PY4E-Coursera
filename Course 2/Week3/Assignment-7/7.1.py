# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("Enter Proper File Name")
lines=fh.read()
caps=lines.upper()
print(caps.strip())
    