#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests

requests.get('xx')
requests.post('xx')
# 一样的
requests.request(method='get', url='xx')
requests.request(method='post', url='xx')

'''
method: 请求方式
url：地址
params：URL中传入参数
headers：请求头
cookies：Cookies
data：数据
json: 数据

'''

requests.get(
    url='http://www.garster.cn',
    params={'nid': 1, 'name': 'x'},
    # 相当于params也是传参的
    # http://www.garster.cn?nid=1&name=x
    headers={},
    cookies={},
)

requests.post(
    url='ss',
    data={},
    headers={},
    cookies={},
)
############################################
#json参数
'''
请求头：http://www.garster.cn   headers ....
请求体：参数为data时是这样的"name=garden&age=18"    
       把data换成json参数后就变成'{"name":"garden","age":18}'
'''
requests.post(
    url='http://www.garster.cn',
    data={
        'name':'garden',
        'age':18
    },
    headers={},
    cookies={},
)
#############################################

