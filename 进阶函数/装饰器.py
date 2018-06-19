#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 为了符合开放封闭原则
# 可以用装饰器进行加功能
user_status = False


def login(func):
    def inner(*args,**kwargs):
        global user_status
        _username = 'garden'
        _password = 'garden'
        if (user_status == False):
            username = input('user:').strip()
            password = input('password:').strip()
            if (username == _username and password == _password):
                print('welcome!')
                user_status = True
            else:
                print('username or password wrong!')
        else:
            print('用户已登录，验证通过!')
        if user_status:
            func(*args,**kwargs)

    return inner


@login
def Home():
    print('===首页===')


@login
def American():
    print('===欧美===')


@login
def China():
    print('===国产===')

@login
def Japanese(stely):
    print('===日本===', stely)


Home()
Japanese('3p')
American()
China()
