#!/usr/bin/env python
# _*_ coding: utf-8 _*_


# 只要含有yield关键字的函数都是生成器函数
# yield和return不可以共用
# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#
# # 生成器函数：执行后会得到一个生成器作为返回值
# g = generator()
# ret = g.__next__()
# print(ret)

def wahaha():
    for i in range(2000):
        yield '娃哈哈{0}'.format(i)
g = wahaha()
for i in g:
    print(i)