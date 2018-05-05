import urllib.request

def download(url):
    response = urllib.request.urlopen(url,timeout=10)
    print(type(response))
    print(response.info())

print(download("http://www.baidu.com"))

user_agent= "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
