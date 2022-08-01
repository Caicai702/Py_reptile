# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:28:06 2022

@author: zsj
"""

# （1）用urllib来获取源码 urllib.request：用于打开和阅读URL
#https://cn.bing.com/search?q=周杰伦&sex=男
import urllib.parse

data={
      'q':'周杰伦',
      'sex':'男'   
      }

a=urllib.parse.urlencode(data)
print(a)