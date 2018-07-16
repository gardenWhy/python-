#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.douyin.com/share/user/95420758225?share_type=link'  # 96488770253/6556303280/67561351000

# ###################### 1. 根据url获取用户ID #########################
user_id = re.findall('share/user/(.*)\?', url)[0]

# ###################### 2. 根据用户ID获取签名 #########################
p = os.popen('node byted-acrawler.js %s' % user_id)
signature = p.readlines()[0]
print(signature)
# signature = p.readlines()[0]

# ###################### 3. 获取抖音用户发送过的所有的视频 #########################
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
}
dytk_ret = requests.get(
    url=url,
    headers=headers
)
dytk_soup = BeautifulSoup(dytk_ret.text,'lxml')
dytk_script = dytk_soup.find_all('script',attrs={'type':'text/javascript'})
dytk_str = str(dytk_script[-1])
dytk = re.findall("dytk: '(.*)'",dytk_str)[0]

user_video_list = []

user_video_params = {
    'user_id': str(user_id),
    'count': '21',
    'max_cursor': '0',
    'aid': '1128',
    '_signature': signature,
    'dytk': dytk
}


def get_aweme_list(max_cursor=None):
    if max_cursor:
        user_video_params['max_cursor'] = str(max_cursor)
    res = requests.get(
        url="https://www.douyin.com/aweme/v1/aweme/post/",
        params=user_video_params,
        headers=headers
    )
    content_json = res.json()
    aweme_list = content_json.get('aweme_list', [])
    user_video_list.extend(aweme_list)
    if content_json.get('has_more') == 1:
        return get_aweme_list(content_json.get('max_cursor'))


get_aweme_list()

print("该用户发布过抖音", user_video_list)
'''
# ###################### 4. 获取抖音赞过的所有视频 #########################

favor_video_list = []

favor_video_params = {
    'user_id': str(user_id),
    'count': '21',
    'max_cursor': '0',
    'aid': '1128',
    '_signature': signature,
    'dytk': dytk
}


def get_favor_list(max_cursor=None):
    if max_cursor:
        favor_video_params['max_cursor'] = str(max_cursor)
    res = requests.get(
        url="https://www.douyin.com/aweme/v1/aweme/favorite/",
        params=favor_video_params,
        headers=headers
    )
    content_json = res.json()
    aweme_list = content_json.get('aweme_list', [])
    favor_video_list.extend(aweme_list)
    if content_json.get('has_more') == 1:
        return get_favor_list(content_json.get('max_cursor'))


get_favor_list()

print("该用户赞过抖音", favor_video_list)
'''
# ###################### 5. 下载抖音 #########################

base_download_folder = os.path.join('download', user_id)
if not os.path.isdir(base_download_folder):
    os.mkdir(base_download_folder)

# 下载自己的视频
user_download_folder = os.path.join(base_download_folder, 'user')
if not os.path.isdir(user_download_folder):
    os.mkdir(user_download_folder)

for aweme in user_video_list:
    if aweme.get('video', None):
        video_id = aweme['video']['play_addr']['uri']

        file_name = video_id + ".mp4"
        file_path = os.path.join(user_download_folder, file_name)

        response_video = requests.get(
            url='https://aweme.snssdk.com/aweme/v1/play/',
            params={
                'video_id': video_id,
            },
            stream=True,
        )
        print('正在下载',video_id)
        with open(file_path, 'wb') as fh:
            for chunk in response_video.iter_content(chunk_size=1024):
                fh.write(chunk)
'''
# 下载赞过的视频
snum = input('是否下载点赞视频?（1)')
if snum == 1:
    favor_download_folder = os.path.join(base_download_folder, 'favor')
    if not os.path.isdir(favor_download_folder):
        os.mkdir(favor_download_folder)

    for aweme in favor_video_list:
        if aweme.get('video', None):
            video_id = aweme['video']['play_addr']['uri']

            file_name = video_id + ".mp4"
            file_path = os.path.join(favor_download_folder, file_name)

            response_video = requests.get(
                url='https://aweme.snssdk.com/aweme/v1/play/',
                params={
                    'video_id': video_id,
                },
                stream=True,
            )
            with open(file_path, 'wb') as fh:
                for chunk in response_video.iter_content(chunk_size=1024):
                    fh.write(chunk)
else:
    pass
'''