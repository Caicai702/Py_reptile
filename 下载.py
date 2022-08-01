# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:36:20 2022

@author: zsj
"""

# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
import urllib.request

#1. 下载网页
#url_page='http://www.baidu.com'
#url代表下载的路径 filename文件的名字
#urllib.request.urlretrieve(url_page,'baidu.html')
#2. 下载图片
#url_img='https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fblog%2F202108%2F08%2F20210808003345_65b5f.thumb.1000_0.jpg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1661568545&t=ec82c7e6172639fd11a143339fca03b8'
#urllib.request.urlretrieve(url_img,'张子枫.png')
#3. 下载视频
#url='https://vd3.bdstatic.com/mda-ngt3dyc6q2avj757/sc/cae_h264/1658975277763566754/mda-ngt3dyc6q2avj757.mp4?v_from_s=hkapp-haokan-hna&auth_key=1658978654-0-0-afb4ef58a68842f2aa84dd9d76f2f6d7&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=3254907112&vid=16289609508193344124&abtest=103578_1-103742_3&klogid=3254907112'
#urllib.request.urlretrieve(url,'张子枫.mp4')