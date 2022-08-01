# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:22:38 2022

@author: zsj
"""

#数据采集时绕过登录 进入到某个页面 主要是cookit
url='https://weibo.com/p/1005055987786107/info'
headers={
'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#'accept-encoding':' gzip, deflate, br',
'accept-language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'cache-control':' max-age=0',
'cookie':'这里放自己的cookie',
'sec-ch-ua':' " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile':' ?0',
'sec-ch-ua-platform':' "Windows"',
'sec-fetch-dest':' document',
'sec-fetch-mode':' navigate',
'sec-fetch-site':' same-origin',
'sec-fetch-user':' ?1',
'upgrade-insecure-requests':' 1',
'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'     }
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
content=response.read().decode('utf-8')
with open('weibo.html','w',encoding='utf-8')as fp:
    fp.write(content)
