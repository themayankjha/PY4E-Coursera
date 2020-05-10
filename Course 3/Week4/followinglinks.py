#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
count = input("Enter Count: ")
try: 
    count=int(count) 
except: 
    print("Enter Valid Count")
position = input("Enter Position: ")
try:
    position=int(position) 
except: 
    print("Enter Valid Count")

for x in range(count+1):
    print("Reading URL:", url)
    html=urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")
    tags=soup('a')
    urltag=tags[position-1]
    url=urltag.get('href', None)