# encoding:utf-8
import  urllib2
import urllib
import lxml
import lxml.etree
import re

def  download(url):
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers) #请求，修改，模拟http
    data = urllib2.urlopen(request).read() #打开请求，抓取数据
    mytree = lxml.etree.HTML(data)

    datalist = mytree.xpath("//*[@class=\"datalist\"]//tr//td//text()") #抓取职位个数
    print datalist
    for linedata in datalist:
        print linedata



# <div class="rt">
#                 共6308条职位
#             </div>

download("http://quote.stockstar.com/fund/stock_3_1_2.html")