# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:22:03 2022

@author: zsj
"""

import urllib.request
import urllib.parse
import json

url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=playable&start=0&limit=20'
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
        }

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
#响应
response = urllib.request.urlopen(request)
#得到结果
content=response.read().decode('utf-8')
obj=json.loads(content)
#print(obj)
#下载数据
#文件保存的是gbk的编码 如果想保存则需修改编码
fp=open('douban.json','w',encoding='utf-8')
fp.write(content)

#那么怎么下载前10页数据呢

#(1)请求对象的定制
#(2)获取响应的数据
#(3)下载数据
#对象定制
def create_request(page):
    url_b='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=playable&'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
        }
    data={
            'start':(page-1)*20,
            'limit':20
            }
    #post 请求的参数必须要进行编码
    data=urllib.parse.urlencode(data)   
    url=url_b+data
    return urllib.request.Request(url=url,headers=headers)

#获取相应数据
def get_content(request):
      response = urllib.request.urlopen(request)  
      content=response.read().decode('utf-8')
      return content
  
#下载数据
def dowloan(page,content):
     fp=open('douban'+str(page)+'.json','w',encoding='utf-8')
     fp.write(content)     
#程序的入口  if  __name__  == __main__  
if  __name__  == '__main__':
    start_page=int(input('开始的页数'))
    end_page=int(input('结束的页数'))  
    for page in range(start_page,end_page+1):
        dowloan(page,get_content(create_request(page)))
       
    