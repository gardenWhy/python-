#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 为了符合开放封闭原则
# 可以用装饰器进行加功能
user_status = False


def login(auth_type):
    def outter(func):
        def inner(*args, **kwargs):
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
                func(*args, **kwargs)
        return inner
    return outter



def Home():
    print('===首页===')



def American():
    print('===欧美===')



def China():
    print('===国产===')


@login('qq')
def Japanese(stely):
    print('===日本===', stely)



Japanese('3p')
