# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:08:50 2022

@author: zsj
"""

# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
import urllib.request
import urllib.error
# （2）上链接，你要访问的地址
url='http://www.123456douban.com'

headers={
         'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
       # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
       # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
  }

try:
#  （3）模拟浏览器打开网页，向服务器发送请求 response：响应
    response = urllib.request.urlopen(urllib.request.Request(url=url,headers=headers))

#   （4）获取响应的页面源码并且解码（read返回的是二进制数据）
    content = response.read().decode('utf-8')

#
    print(content)
    
except urllib.error.HTTPError:
    print('网页走丢啦~')
except urllib.error.URLError:
    print('没找到该网页')    