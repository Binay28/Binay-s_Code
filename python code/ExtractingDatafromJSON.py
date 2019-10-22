import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address=input("enter the URl : ")
#if len(address)<1:break
url=urllib.request.urlopen(address,context=ctx)
Json=url.read().decode()
info = json.loads(Json)
#print(info["comments"])
#print('User count:', len(info))
s=0
for item in info["comments"]:
    #print('Name:', item["name"])
    #print('Id:', item['id'])
    #print('Attribute:', item['x'])
     print("Count :",item["count"])
     s+=int(item["count"])
print(s)
