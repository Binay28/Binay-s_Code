import urllib.request,urllib.parse,urllib.error
fhand =urllib.request.urlopen('https://thelawdictionary.org/letter/a/')
for line in fhand:
    print(line.decode().strip())
