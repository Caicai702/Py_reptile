# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:28:15 2022

@author: zsj
"""

# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
import urllib.request

url='https://www.baidu.com'

#url组成   https://www.baidu.com/s?wd=周杰伦
#http/https         www.baidu.com         80/443         s           wd=周杰伦      #
#协议                 主机              端口号           路径          参数         描点

#ua放到字典里，浏览器ua标识是网站通过对ua标示的判别,可按相应的格式进行网页的布局调整,使用户获得更好的浏览体验
headers={
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
        }

#请求对象的定制,不然就会被反爬取（模拟浏览器）
request = urllib.request.Request(url=url,headers=headers)
#模拟浏览器打开网页，向服务器发送请求 response：响应
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)