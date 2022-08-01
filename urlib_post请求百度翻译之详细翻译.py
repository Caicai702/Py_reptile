# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:07:36 2022

@author: zsj
"""

import urllib.request
import urllib.parse
import json


url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers={
        #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
      
#'Accept':' */*',
#'Accept-Encoding':' gzip, deflate, br',
#'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#'Acs-Token':' 1658991609277_1659060787121_fsWQ2EFSY5EudlByr1bbmtl1Us7FDEtsRoahOjCA5ynG81+pjF77fToupV8ALD7lhn7yP5rIgrlx5hfiEqxNBWPYsT/WSdnRnVmLnybozKe8FWp1sYgIRToGdQXPPwMAyknqRyWB+TfQU1zvGtWyn2cxKpzKhb+BB/QOdCW/9UUVmEogwnfx+yBpRZxhv3fYdR+XYZWi5LhK3uSm/PfMMHeuN8yarcW/DYtoyY6blyP65B4BIROeoBAP/K1USN0Wor8SHA+VDhfltbqpEJ+PxAzTtAwFdEYFndfJSwmP0h1NI9MFTw/KMAqIfCNK8a97HUcwhNMSsSiRLmyLe0nKSA==',
#'Connection':' keep-alive',
#'Content-Length':' 135',
#'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':' REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1634311751; __yjs_duid=1_7a7f627fa52ce2a8438924dcb620a1df1634401264087; BDUSS=13d01PSFdhV0dyWGRoZ0RpTWxRei1vYjIwSkowN0hkVGEyM0ViQ3lDSktVTDFoRVFBQUFBJCQAAAAAAAAAAAEAAACBdS2tzuLTw2hlYXJ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAErDlWFKw5VhM0; BDUSS_BFESS=13d01PSFdhV0dyWGRoZ0RpTWxRei1vYjIwSkowN0hkVGEyM0ViQ3lDSktVTDFoRVFBQUFBJCQAAAAAAAAAAAEAAACBdS2tzuLTw2hlYXJ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAErDlWFKw5VhM0; BIDUPSID=977DA22423CE9099CF7E8B858ECFFF5F; BAIDUID=0B8ED1E01F898036F64DA8DA9C0E1D8A:FG=1; BAIDUID_BFESS=0B8ED1E01F898036F64DA8DA9C0E1D8A:FG=1; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1659057254; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1659060675; ab_sr=1.0.1_NGUyZDU3N2RmMTkxMDY3MDI5MGFhNTNlOGNjYmY1ZDQ1MTBkNzlkOTdlNzUwOTYwMjMyYWExOGZlMTZmNmE2OTk3Yzc5ZDcxMjI4NTM2OWUzMWVkMTEwZjRhZGJmZmFmY2YzNDcyNWU5MTJiMjljMWM0OGZjYTIxNGMwNDNlNmVkNjgzZjgxNzRmOGE3Yzg5ZGU5OTM4N2NhMTY5M2E5ZWI1NWZhNDY3ZDE0OWVhYzMyNDVjZDdmNWUzMWJlZTJj',
#'Host':' fanyi.baidu.com',
#'Origin': 'https://fanyi.baidu.com',
#'Referer': 'https://fanyi.baidu.com/',
#'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
#'sec-ch-ua-mobile':' ?0',
#'sec-ch-ua-platform': '"Windows"',
#'Sec-Fetch-Dest': 'empty',
#'Sec-Fetch-Mode': 'cors',
#'Sec-Fetch-Site': 'same-origin',
#'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
#'X-Requested-With': 'XMLHttpRequest'
        }
data={
      'from':'en',
      'to':'zh',
      'query':'hello',
      'transtype':'realtime',
      'simple_means_flag':'3',
      'sign':'54706.276099',
      'token':'af390587963be6a2005b58cf41d9b94f',
      'domain':'common'
      }

#post 请求的参数必须要进行编码
data=urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求

response = urllib.request.urlopen(request)
content=response.read().decode('utf-8')




obj=json.loads(content)
print(obj)