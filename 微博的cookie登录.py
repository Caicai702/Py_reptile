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
'cookie':'login_sid_t=6f87e8775d28ce64e89437256655128a; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=5468084505293.436.1659317578551; SINAGLOBAL=5468084505293.436.1659317578551; ULV=1659317578555:1:1:1:5468084505293.436.1659317578551:; wb_view_log=1536*8641.25; WBtopGlobal_register_version=2022080109; SUB=_2A25P410mDeRhGeNH41UW-CjNyzuIHXVsmcnurDV8PUNbmtAKLWLTkW9NSnjxpHPU5r3Qgq8pW2IB3uJAOPrB7bKX; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56yuUOKYyxk0JRQRe8iH2Q5JpX5o275NHD95Qf1KnNS0nceK5NWs4Dqcji-cQ41KM7eLvA; ALF=1659922422; SSOLoginState=1659317622; wvr=6; wb_view_log_5987786107=1536*8641.25; PC_TOKEN=d59b33c58e; webim_unReadCount=%7B%22time%22%3A1659320082060%2C%22dm_pub_total%22%3A106%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A1%2C%22allcountNum%22%3A253%2C%22msgbox%22%3A0%7D',
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
