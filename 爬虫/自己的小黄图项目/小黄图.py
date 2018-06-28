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
        title = a.get('title')
        div = a.find('div', attrs={'class': 'image'})
        img_src = div.find('img').get('src')
        ret_img = requests.get(img_src).content
        print(img_src)  # 图片地址
        print(title)  # 标题
        print(firs_url + a.get('href'))  # 网址
        print('=' * 30)
        create_dir(title, ret_img)


def create_dir(title, ret_img):
    if '?' in title:
        title = title.replace('?', ' ')  # 防止文件夹目录出现特殊字符

    file_name = '%s\\%s\\title.jpg' % (os.getcwd(), title)
    if not os.path.exists(title):
        os.makedirs(title)
    with open(file_name, 'wb') as f:
        f.write(ret_img)


def getzip():
    pass


def next():
    pass


def main():
    geturl()


if __name__ == '__main__':
    main()
