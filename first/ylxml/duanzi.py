# encoding:utf-8
import  urllib2
import urllib
import lxml
import lxml.etree
import re
def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers) #请求，修改，模拟http
    data = urllib2.urlopen(request).read() #打开请求，抓取数据
    mytree = lxml.etree.HTML(data)
    datalist = mytree.xpath("//*[@class=\"piclist longList\"]//a[@href!=\"/article/\"]//text()")
    print datalist
    for linedata in datalist:
        print linedata

    datalist = mytree.xpath("//*[@class=\"picList longList\"]//div[@class=\"f18 mb20\"]//p//text()")
    print datalist
    for linedata in datalist:
        print linedata

    datalist = mytree.xpath("//*[@class=\"piclist longList\"]//div[@class=\"f18 mb20\"]//text()")
    print datalist
    for linedata in datalist:
        print linedata


download("http://www.neihan8.com/article/list_5_10.html")