#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 作用域
# python中函数就是一个作用域 {JavaScript}
# c# Java中作用域{}
# 定义完成后，作用域就已经生成，作用域链向上查找

def func1():
    age = 73

    def fun2():
        print(age)

    return fun2


val = func1()
print(val)
