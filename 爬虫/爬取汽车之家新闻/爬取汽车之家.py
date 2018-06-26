#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
import requests
from bs4 import BeautifulSoup
import lxml

# 1. 下载页面
ret = requests.get('https://www.autohome.com.cn/news/')
# print(ret.content) # 输出二进制形式
# ret.encoding = 'GBK' # 转换编码
# print(ret.text) # 输出文本形式
# print(ret.apparent_encoding) #帮检测是什么编码

ret.encoding = ret.apparent_encoding
# print(ret.text)

# 2. 解析：获取想要的指定内容beautifulsoup
soup = BeautifulSoup(ret.text, 'html.parser')
div = soup.find(name='div', id='auto-channel-lazyload-article')  # find 是找匹配成功的第一个
li_list = div.find_all(name='li')  # find_all是找所有匹配成功的

for li in li_list:
    h3 = li.find(name='h3')  # 找h3标签
    if not h3:
        continue
    a = li.find(name='a')
    p = li.find(name='p')  # 找p标签
    img = li.find('img')
    src = img.get('src')
    file_name = src.rsplit('__',maxsplit=1)[1] # rsplit()方法和split()类似，只不过是从字符串最后开始分割，maxsplit为最大分割次数
    ret_img = requests.get('https:' + src)

    path = os.getcwd()
    with open(path+'\\img\\'+file_name,'wb') as f:
        f.write(ret_img.content)

    print(h3.text, a.get('href'))  # text拿文本
    print(p.text)
    print('=' * 20)
    # a = li.find(name='a')
    # print(a.get('href')) # get 取单独的标签属性 还有个attrs是把所有属性全部取出来
