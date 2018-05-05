#encoding:utf-8
import re

# mystr = """<span class=\"search_yx_tj\">
#         共<em>1537</em>个职位满足条件
#     </span>"""
#
# restr = "<em>(\\d+)</em>"
# regex = re.compile(restr,re.IGNORECASE)
# mylist = regex.findall(mystr)
# print mylist[0]


# import urllib2
# def download(url):
#     return urllib2.urlopen(url).read()
#
# url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=python&sm=0&p=1"
# print download(url)

import selenium #测试框架
import selenium.webdriver #模拟浏览器

def getnumbername(searchname):
    url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw="+searchname+"&sm=0&p=1"
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    pagesource = driver.page_source
    restr = "<em>(\\d+)</em>"
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()
    return mylist[0]

# print getnumbername("python")
pythonlist = ["python","python 运维","测试","python web","java","区块链"]

for name in pythonlist:
    print name,getnumbername(name)
