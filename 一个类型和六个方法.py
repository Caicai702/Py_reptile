# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:17:51 2022

@author: zsj
"""

# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
import urllib.request

# （2）上链接，你要访问的地址
url='http://www.baidu.com'

#  （3）模拟浏览器打开网页，向服务器发送请求 response：响应
response = urllib.request.urlopen(url)


#一个类型和6个方法
#1.response类型：HTTPResponse
#print(type(response))

#2.一个一个字节来读
#content = response.read()

#3.返回n个字节，当n=5时
#content = response.read(5)

#4. 按行来读
#content = response.readline()
#content = response.readlines()

#5. 返回状态码 如果是200 则逻辑没错
#print(response.getcode())


#6. 返回url地址
#print(response.geturl())

#7. 返回状态信息
print(response.getheaders())