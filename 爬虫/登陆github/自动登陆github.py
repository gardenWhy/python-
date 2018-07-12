#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup
##############获取token&cookies##############
ret = requests.get(
    url='https://github.com/login'
)
soup = BeautifulSoup(ret.text, 'lxml')
token = (
    soup.find(name='input',
              attrs={'name': 'authenticity_token'}).get('value'))
cookies_dict = ret.cookies.get_dict()
# print(token)
################登陆获取username#################
r2 = requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': token,
        'login': 'email',
        'password': 'password'
    },
    cookies=cookies_dict
)
soup2 = BeautifulSoup(r2.text, 'lxml')
username = soup2.find('strong', attrs={'class': 'css-truncate-target'}).text
####################拼接url请求个人信息页面#####################
userUrl = 'https://github.com/' + username
r3 = requests.get(userUrl, cookies=r2.cookies.get_dict())
soup3 = BeautifulSoup(r3.text,'lxml')
fullname = soup3.find('span',attrs={'class':'p-name vcard-fullname d-block overflow-hidden'}).text
username = soup3.find('span',attrs={'class':'p-nickname vcard-username d-block'}).text
bio = soup3.find('div',attrs={'class':'d-inline-block mb-3 js-user-profile-bio-contents'}).find('div').text
org = soup3.find('span',attrs={'class':'p-org'}).find('div').text
email = soup3.find('a',attrs={'class':'u-email'}).text
#############################################################
print('''
#########UserInfo#########
fullname:{}
username:{}
bio:{}
organization:{}
email:{}
#########UserInfo#########
'''.format(fullname,username,bio,org,email))
