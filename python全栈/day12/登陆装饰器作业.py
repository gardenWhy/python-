#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from functools import wraps

flag = 0


def login(func):
    @wraps(1)
    def inner(*args, **kwargs):
        global flag
        if flag == 0:
            user = input('请输入你的账号:')
            passwd = input('请输入你的密码：')
            if user == 'garden':
                if passwd == 'garden':
                    print('登陆成功！')
                    flag = 1
                else:
                    print('账号或密码错误')
                    return 0
            else:
                print('账号或密码错误！')
                return 0
        ret = func(*args, **kwargs)
        return ret

    return inner


@login
def chinese():
    print('====欢迎进入国内专区====')


@login
def jp():
    print('====欢迎进入日本专区====')
    print('welcome')


if __name__ == '__main__':
    chinese()
    jp()
