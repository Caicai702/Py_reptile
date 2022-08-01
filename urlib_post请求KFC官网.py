# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 08:30:12 2022

@author: zsj
"""
import urllib.request
import urllib.parse
import json




#对象定制
def create_request(page):
   # url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'    #城市检索
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'  #关键字检索
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
        }
    data={
            'cname': '',#城市检索
            'pid': '',
            'keyword':'清远',#关键字检索
            'pageIndex': page,
            'pageSize': '10'
            }
    #post 请求的参数必须要进行编码
    data=urllib.parse.urlencode(data).encode('utf-8')   

    return urllib.request.Request(url=url,headers=headers,data=data)

#获取相应数据
def get_content(request):
      response = urllib.request.urlopen(request)  
      content=response.read().decode('utf-8')
      return content
  
#下载数据
def dowloan(page,content):
     fp=open('KFC'+str(page)+'.json','w',encoding='utf-8')
     fp.write(content) 
     
#程序的入口  if  __name__  == __main__  
if  __name__  == '__main__':
    start_page=int(input('开始的页数'))
    end_page=int(input('结束的页数'))  
    for page in range(start_page,end_page+1):
        dowloan(page,get_content(create_request(page)))
        
        