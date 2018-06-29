#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup

ret = requests.get(
    url='https://github.com/login'
)
soup = BeautifulSoup(ret.text, 'lxml')
token = (
    soup.find(name='input',
              attrs={'name': 'authenticity_token'}).get('value'))
# print(token)
r2 = requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': token,
        'login': 'email',
        'password': '123'
    }
)
print(r2.text)
