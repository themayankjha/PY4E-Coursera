#!/usr/bin/python3
#imports
import json
import urllib.request,urllib.parse, urllib.error
import ssl

#ignore ssl
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#code
add=0
while True :
    url=input("Enter URL: ")
    if len(url)<1 : break
    print("Retreaving Url")
    data=urllib.request.urlopen(url,context=ctx).read()
    print("Retrieved", len(data), "characters")
    data=json.loads(data)
    for user in data['comments'] :
        print("Count:",user['count'])
        add=add+int(user['count'])
    print("Final Count is: ", add)
    break
    
