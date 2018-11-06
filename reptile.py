#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from lxml import html
url='https://movie.douban.com/' #需要爬数据的网址
page=requests.Session().get(url)
tree=html.fromstring(page.text)
result=tree.xpath('//li[@class="title"]//a/text()') #获取需要的数据,
                                                    #1.//td:这个相当于指定的大目录
                                                    #2.[@class="title"]:这个相当于指定的目录
                                                    #3.//a:这个相当于最小的目录
                                                    #4./text():这个是提取中的数据

print(result)