#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup

head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.87 Safari/537.36'}

url = 'https://dig.chouti.com/login'
ret = requests.get('https://dig.chouti.com/', headers=head)
cookie_dict = ret.cookies.get_dict()

response = requests.post(
    url=url,
    data={
        'phone': '86xxxxxxxxphone',
        'password': 'password',
        'oneMonth': '1'
    },
    cookies=cookie_dict,
    headers=head
)

soup = BeautifulSoup(ret.text,'lxml')
items = (
    soup.find(attrs={'id': 'content-list'}).
        find_all(attrs={'class':'item'})
)

for item in items:
    id = item.find(attrs={'class':'news-pic'}).find('img').get('lang')
    if not id:
        continue

    d1 = requests.post(
        url='https://dig.chouti.com/link/vote?linksId=%s' % (id),
        headers=head,
        cookies=cookie_dict
    )
    print(d1.text)
