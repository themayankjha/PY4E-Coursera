#!/usr/bin/python3
name=input("Enter File :")
if len(name) < 1 : name="mbox-short.txt"
handle= open(name)
lst=list()
emails = list()
mailcount=dict()
topcount = 0
topkey = None
for line in handle :
    if line.startswith("From:") : continue
    if not line.startswith("From"):continue
    lst=line.split()
    emails.append(lst[1])
for email in emails :
    mailcount[email]= mailcount.get(email,0)+1
for mail in mailcount :
    if mailcount[mail]>topcount :
        topkey = mail
        topcount = mailcount[mail]
print(topkey,topcount)
    
        
