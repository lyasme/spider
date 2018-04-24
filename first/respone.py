import urllib.request

def download(url):
    response = urllib.request.urlopen(url,timeout=10)
    print(type(response))
    print(response.info())

print(download("http://www.baidu.com"))