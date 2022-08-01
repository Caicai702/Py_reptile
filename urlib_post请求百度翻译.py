# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 09:19:36 2022

@author: zsj
"""

#post请求  https://fanyi.baidu.com/sug


import urllib.request
import urllib.parse
import json
url='https://fanyi.baidu.com/sug'

s=input("请输入你要查询的单词：")
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
        }

data={
      'kw':s
      }

#post 请求的参数必须要进行编码
data=urllib.parse.urlencode(data).encode('utf-8')
#print(data)

#
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求

response = urllib.request.urlopen(request)
content=response.read().decode('utf-8')
obj=json.loads(content)
print(obj)

#总结以下 post请求方式的参数 必须编码 data=urllib.parse.urlencode(data).encode('utf-8')