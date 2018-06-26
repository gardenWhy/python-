#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup
import lxml
import os


def geturl():
    firs_url = 'https://hmghmg.xyz'
    url = 'https://hmghmg.xyz/mg/'
    ret = requests.get(url)
    ret.encoding = ret.apparent_encoding
    soup = BeautifulSoup(ret.text, 'lxml')
    ul = soup.find(name='ul', attrs={'class': 'file_list'})
    li_list = ul.find_all('li')
    for li in li_list:
        a = li.find('a')
        print(a.get('title'))  # 标题
        print(firs_url + a.get('href'))  # 网址
        print('=' * 30)

def getzip():
    pass

def next():
    pass

def main():
    geturl()


if __name__ == '__main__':
    main()
