# Use the file name mbox-short.txt as the file name
final=0
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(":")
    data=line[pos+1:]
    data=data.strip()
    try:
        data=float(data)
    except:
        print("Failed Data Parsing")
        exit(1)
    final=final+data
    count=count+1
print("Average spam confidence:",final/count)
