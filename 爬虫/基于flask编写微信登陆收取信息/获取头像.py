#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests

ret = requests.get(
    url='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgeticon?seq=1528193111&username=@9f2ac2f687e641a3e065ff94f7e66db68976a0d7bce6e37d9174d321f0482298&skey=@crypt_4d5a4e5f_185e371719694e34acb261e2c64bb1c9',
    headers={
        'host':'wx2.qq.com',
        'Referer':'https://wx2.qq.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Cookie':'session=.eJwljMFugzAQRP_F5x4w2GAiRapRU7UH0gNUarlYxmxtQ0kIJqEkyr_XSbSXmZ15c0EHtW8ArdCsBl6fhDB6vUZPaLKqg0k0Vk1odUHW6VEuTsnfWxf7Qg_OSX1z3gzSOfFA_OOb04zt8-4rrwwvMwM9-9A6j3DQHc7j50sB26SEqunD4rzbtHpTtvk2W96cKUzk3k9-cLwPBV65DhYvn9W4DJMgDZUE6I_AjEKU4ASncUogIlLVYYwhVDGpa6xST85_zjYefU3ipeVVYNr52Je8vEdHu_MRi_2xNKToev0HUDRTrA.DiNR5A.kbvv7T8u1O83_lTHnsIlU4EgaB8'
    }
)

print(ret.text)