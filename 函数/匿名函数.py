#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc(x, y):
    return x * y


func = lambda x, y: x * y  # 声明一个匿名函数
# lambda匿名函数是不能写复杂的逻辑判断的，只能写简单的函数
print(func(3, 8))

data = list(range(10))
print(data)


def f2(n):
    return n * n


print(list(map(lambda x: x * x, data)))  # 可以写一个函数在第一参数，后面的列表的值都放前面的函数执行一遍
