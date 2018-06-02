#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
#
# def recursion(n):
#     print(n)
#     recursion(n + 1)
#
# recursion(1)

def cal(n):
    print(n)
    return cal(n + 1)
#尾递归,调用下一层的同时就退出了
cal(1)