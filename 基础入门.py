# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:01:03 2022

@author: zsj
"""
# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
import urllib.request

# （2）上链接，你要访问的地址
url='http://www.baidu.com'

#  （3）模拟浏览器打开网页，向服务器发送请求 response：响应
response = urllib.request.urlopen(url)

#   （4）获取响应的页面源码并且解码（read返回的是二进制数据）
content = response.read().decode('utf-8')

#
print(content)