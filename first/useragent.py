#coding:utf-8

import urllib2
def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(url,headers=headers) #发起请求
    data = urllib2.urlopen(request).read() #打开请求抓取数据
    return data

url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&p=1&isadv=0" #urlopen只能处理http.不可以处理https
print download(url)