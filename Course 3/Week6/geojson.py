#!/usr/bin/python3
#imports
import urllib.request, urllib.parse,urllib.error
import json
import ssl
#ignore ssl errors
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE
#code
serviceurl='http://py4e-data.dr-chuck.net/json?'
while True:
    address=input("Enter Location: ")
    if len(address) < 1 : break
    params = dict()
    params['address'] = address
    params['key'] = 42
    url = serviceurl + urllib.parse.urlencode(params)
    print('Retreaving:',url)
    
    data=urllib.request.urlopen(url,context=ctx).read().decode()
    print("Retrieved",len(data),"characters")
    
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js['status'] != 'OK':
        print("Data Conversion Faliure")
        print(data)
        continue
    placeid=js['results'][0]['place_id']
    print('place id is', placeid)
