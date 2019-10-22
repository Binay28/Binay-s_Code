import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
#ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url='https://thelawdictionary.org/letter/'
pg='page/'
for alpha in range(ord('a'),ord('z')+1):
   # for i in range(10):
        html=urllib.request.urlopen(url+chr(alpha)+pg+str(1)+'/',context=ctx).read()
        soup=BeautifulSoup(html,'html.parser')
#retrieve the data
        tags=soup('h2')
        for tag in tags:
   # print(tag.get('title',None))
            name_box=soup.find('h2',attrs={'class':'title'})
            name=name_box.text.strip()
            print(name)
