#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
修改个人信息程序
在一个文件里存多个人的个人信息，如以下
用户，密码，名字，年龄，职业
garden,garden123,嘎登,24,Engineer
rain,df2@432,哈哈,25,Teacher
1、输入用户名密码，正确后登陆系统，打印
    1.修改个人信息
    2、打印个人信息
    3、修改密码
2、每个选项写一个方法
3、登陆时输错3次退出程序
'''


def login():
    print('''
    *******************************
    *                             *
    * !!!WELCOME GARDEN SYSTEM!!! *
    * !!!   ENJOING YOURSELF  !!! *
    *                             *
    *******************************
    ''')
    print('请输入你的账户密码')
    for i in range(3):
        user = input('user:').strip()
        password = input('password:').strip()
        with open('information.txt', encoding='utf-8') as f:
            p = f.read().split('\n')
            for r in p:
                u, pa = r.split(',')[:2]
                if u == user and password == pa:
                    return u
            print('账户或密码错误！')


def changeinfo():
    pass


def output(uid):
    with open('information.txt', encoding='utf-8') as f:
        p = f.read().split('\n')
        for r in p:
            user, passwd, name, age, job = r.split(',')
            if user == uid:
                break
    print('''
    ====garden====
        name:%s
        age:%s
        job:%s
    ====garden====
    ''' % (name, age, job))


def changepasswd():
    pass


uid = login()
output(uid)
print(uid)
