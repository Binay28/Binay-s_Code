import urllib.request,urllib.parse,urllib.error
fhand =urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
#html=fhand.read()
headers=fhand.info()
print("E-Tag:",headers['ETag'])
print("Content-Length:",headers['Content-Length'])
print("Last-Modified :",headers['Last-Modified'])
print("Content-Type :",headers['Content-Type'])
print("Cache-Control :",headers['Cache-Control'])
for line in fhand:
    print(line.decode().strip())
