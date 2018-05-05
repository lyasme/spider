#encoding:utf-8
import selenium #测试框架
import selenium.webdriver #模拟浏览器
import re

def getnumbername(searchname):
    url = "https://m.51job.com/search/joblist.php?keyword="+searchname+"&keywordtype=2&jobarea=010000&landmark=0&issuedate=&saltype=&degree=&funtype=&indtype=&jobterm=&cotype=&workyear=&cosize=&lonlat=0%2C0&tubename=&tubeline=&radius=-1"
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    pagesource = driver.page_source
    restr = """(\\d+)"""
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(pagesource)
    # print mylist[0]
    driver.close()
    return mylist[0]

# print getnumbername("python")
pythonlist = ["python","python 运维","测试","python web","java","区块链"]

for name in pythonlist:
    print name,getnumbername(name)
