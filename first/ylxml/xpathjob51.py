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
    # data=data.decode("gbk").encode("utf-8") #乱码
    mytree = lxml.etree.HTML(data)
    # print (mytree.xpath("//*[@class=\"rt\"]/text()"))

    mystr = (mytree.xpath("//*[@class=\"rt\"]/text()"))[0].strip() #抓取职位个数
    print mystr

    regex = re.compile("\d+",re.IGNORECASE)
    mylist = regex.findall(mystr)
    print mylist[0]

# <div class="rt">
#                 共6308条职位
#             </div>

download("https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")