#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # 把函数冻结执行在这一步,函数停在这了,相当于一个断点,
        # 并且把b的值返回给外面的next()
        # 好处是可以把里面的值返回回来
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(30)  # turn function into a generator
next(f)  # first time call next()
next(f)
