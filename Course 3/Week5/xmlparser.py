#!/usr/bin/python3
#imports
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
add=0
#ignore ssl issues
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#code
while True :
    url=input("Enter URL: ")
    if len(url)<1 : break
    print("Retreaving URL :", url)
    data=urllib.request.urlopen(url,context=ctx).read()
    print("Retrieved", len(data),"Characters")
    tree=ET.fromstring(data)
    for item in tree.findall('comments/comment/count'):
        print("Count:",item.text)
        add=add+int(item.text)
    print("Final Sum :", add)        
    break;
