# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:49:21 2022

@author: zsj
"""

# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
import urllib.request
import urllib.parse
# （2）上链接，你要访问的地址
url='https://cn.bing.com/search?'
data={
      'q':'梁晓雪+嘉应'

      }
#https://www.baidu.com/s?wd=%E5%BC%A0%E5%AD%90%E6%9E%AB
#将周杰伦的名字变成Unicode编码的格式 %E5%91%A8%E6%9D%B0%E4%BC%A6
name=urllib.parse.quote('易烊千玺')
a=urllib.parse.urlencode(data)
url=url+a
#请求对象的定制
headers={
         'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
       # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
       # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
  }


request = urllib.request.Request(url=url,headers=headers)
#  （3）模拟浏览器打开网页，向服务器发送请求 response：响应
response = urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
