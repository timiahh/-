# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 23:55:41 2018

@author: Janwee
"""
def g(i):
    page=i*44
    import urllib.request as r
    url='https://s.taobao.com/search?q=%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%BB%91%E9%BE%99%E6%B1%9F&bcoffset=4&p4ppushleft=2%2C48&s={}&ntoffset=4&ajax=true'
    data=r.urlopen(url.format(page)).read().decode('utf-8','ignore')
    import json
    data=json.loads(data)
    a=json.dumps(data)
    f=open('黑龙江.txt','a',encoding='utf-8')
    f.write(a+'\n')
    f.close
for i in range(0,100):
    g(i)
    print(i)