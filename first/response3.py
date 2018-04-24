#coding:utf-8  #urllib.request == urllib2
import urllib2  #python2


def download(url):
    response = urllib2.urlopen(url,timeout=5) #超时
    print(type(response))
    print(response.info()) #包涵网站请求的详细信息
    print (response.read(100)) #read读取全部，read（100）读取全部

try:
    print(download("http://www.google.com"))
except urllib2.URLError as e:
    print("web error",e)
