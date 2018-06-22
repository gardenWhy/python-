#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def range2(n):
    count = 0
    while count < n:
        print('count', count)
        count += 1
        sign = yield count
        # if sign == 'stop':
        #     break
        print("----sign", sign)


new_range = range2(10)
n1 = next(new_range)
new_range.send(None)

# 生成器的创建方式
#     1、列表生成式
#     2、函数

# yield vs return
# return 返回 并终止function
# yield 返回数据，并冻结当前执行的过程
#
# next 唤醒冻结的函数执行过程，并继续执行，直到遇到下一个yield

# 总结：只要函数里有yield，就是函数生成器了
# 如果函数有yield的时候再写个return的话，那是没有办法得到这个return的值的
# new_range.send('stop') 发送stop去yield那
