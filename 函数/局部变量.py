#!/usr/bin/env python
# -*- coding: utf-8 -*-
name = 'Black girl'
names = ['garden', 'Black Girl', 'gaga']


def change_name():
    name = "黑姑娘"

    print("在", name, "里面", id(name))


def func2():
    global name
    # 在函数内改全局变量，global在函数内声明
    name = "粉姑娘"
    print(name, id(name))


def func3():
    names[1] = '粉姑娘'
    del names[2]
    print(names, id(names))


# 字典、列表、集合、对象、等等都可以在函数里修改


# change_name()
# func2()
func3()
print(names, id(names))
