from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import ssl
req = Request('http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='http://py4e-data.dr-chuck.net/comments_52661.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    # Look at the parts of a tag
   # print('TAG:', tag)
   # print('URL:', tag.get('href', None))
   # print('Contents:', tag.contents[0])
   # print('Attrs:', tag.attrs)
    sum+=int(tag.contents[0])
print(sum)

