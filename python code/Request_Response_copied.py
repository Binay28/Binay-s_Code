import urllib.request,urllib.error
class HeadRequest(urllib.request.Request):
    def get_method(self):
        return"HEAD"
myurl= "http://www.pythonlearn.com/code/intro-short.txt"
request=HeadRequest(myurl)
try:
    response=urllib.request.urlopen(request)
    response_headers=response.info()
except urllib.error.HTTPError as e:
    print("Error code: %s" %e.code)
print (response_headers)
