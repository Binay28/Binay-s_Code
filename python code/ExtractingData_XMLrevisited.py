import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("enter the url: ")
Xml= urllib.request.urlopen(url, context=ctx).read()
#if len(url) < 1 :break
print(Xml.decode())
data = ET.fromstring(Xml)
lst = data.findall('comments/comment')
#lst2=int(lst.findall('count').text)
#print(sum(lst2))
s=0
for item in lst :
    s=s+int(item.find('count').text)
   # print(item.find('count').text)
print(s)
