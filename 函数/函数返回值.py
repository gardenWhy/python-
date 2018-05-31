#!/usr/bin/env python
# -*- coding: utf-8 -*-

def stu_register(name, age, course):
    print(name, age, course)

    if age > 22:
        return name
    else:
        return True
        # return
        # 默认返回None
        # return也代表着函数的执行结果，遇到return就代表函数执行结束
        # 函数永远有且只能返回一个值


status = stu_register('garden', 19, '安保')
print(status)
