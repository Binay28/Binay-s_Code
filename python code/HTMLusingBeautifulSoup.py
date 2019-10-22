# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url1='http://py4e-data.dr-chuck.net/known_by_Judah.html'
#html = urllib.request.urlopen(url, context=ctx).read()
html1= urllib.request.urlopen(url1, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
soup= BeautifulSoup(html1,'html.parser')
count=int(input('Enter the count'))
position=int(input('enter the position'))
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    position=position-1
    if position==0:
        url2=urllib.request.urlopen(tag.get('href',None))
        soup2 = BeautifulSoup(url2, 'html.parser')
        tags2=soup2('a')
        for tag in tags2:
            print(tag.get('href',None))
            count=count-1
            if count==0:
                exit()
       # val=tag.get('href',None)
       # for num in range(count):
           #print (val.get('href'))
   
