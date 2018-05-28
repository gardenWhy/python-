#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''数据结构：
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
......
]

功能要求：
基础要求：

1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表

2、允许用户根据商品编号购买商品

3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒

4、可随时退出，退出时，打印已购买商品和余额

5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示


扩展需求：

1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买

2、允许查询之前的消费记录'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

with open('user_pwd.txt', 'r') as f:
    user = f.read().split('\n')
user_list = {}
for r in user:
    name, pwd = r.split(',')
user_list[name] = str(pwd)
with open('user_old.txt', 'r') as f:
    user_old = f.read().split('\n')


def login():
    u = input('请输入你的用户名：')
    p = input('请输入你的密码：')
    if u in user_old:
        pass
    else:
        if u in user_list:
            if user_list[u] == p:
                print("登陆成功!")
                return 11
            else:
                print('登陆失败!')
                return 22
        else:
            print('登陆失败!')
            return 22


def shop(money):
    print('''
    v1.0
    ++++++++++++++++
    。。。购物系统。。。
    ++++++++++++++++
    ''')
    temp_money = money
    shop_car = []
    total_buy = 0
    while True:
        for index, value in enumerate(goods):
            print("商品编号:%s   商品名称:%s   商品价格:%s" % (index, value['name'], value['price']))
        choice = input('请输入你要买的商品编号以加入购物车：')
        if choice.isdigit():
            if int(choice) >= 0 and int(choice) < len(goods):
                shop_car.append(goods[int(choice)])
                print("加入成功!")  # 商品加入购物车
                print('当前购物车为：',shop_car)
                print('==========================================')
        elif choice == 'q':  # 判断是否为退出
            if len(shop_car) > 0:
                for num in range(len(shop_car)):
                    will_buy = shop_car[num]['price']
                    total_buy += will_buy
                    temp_money -= total_buy
                print('++++++++++++++++++++++++++++++++++++++++++')
                print("正在结算中......")
                if temp_money <= 0:
                    print("抱歉，你的余额不足")
                    return money
                else:
                    print('购买完成！')
                    return temp_money
            else:
                print('购物车里没有东西哦！退出系统')
                return money


num = login()
if num == 11:
    your_money = int(input("请输入你的工资:"))
    your_money = shop(your_money)
    print("你的余额为：%d" % (your_money))
