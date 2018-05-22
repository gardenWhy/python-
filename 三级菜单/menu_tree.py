#!/usr/bin/env python
# -*- coding: utf-8 -*-
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}  # 定义菜单
menu_temp = menu  # 中间变量
temp = []  # 中间变量
while 1:
    print(menu_temp.keys())
    n = input("请输入你的要进入的列表名称(输入'b'返回上一层,输入'q'退出此程序):").strip()  # 输入，并且去空格
    if n in menu_temp:
        temp.append(menu_temp)
        menu_temp = menu_temp[n]
    elif n not in menu_temp and n != 'b' and n != 'q':print('请检查输入！')
    elif n == 'b':
        if temp:
            menu_temp = temp[-1]
            temp.pop()
        else:print('已经到达顶层')
    if n == 'q':break
