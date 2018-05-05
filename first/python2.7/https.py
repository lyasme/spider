#coding:utf-8
import urllib2
import urlparse
import ssl

"""
def download(url):
    return urllib2.urlopen(url).read()

print download("https://www.baidu.com")
"""
context=ssl._create_unverified_context() #忽视安全
url = "https://www.baidu.com"
headers = {
"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request,context=context)
print response.read()


