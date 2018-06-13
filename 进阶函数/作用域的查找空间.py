#!/usr/bin/env python
# -*- coding: utf-8 -*-
#作用域查找顺序:LEGB 往上查找


n = 10
def func1():
    n = 20
    print(n)

    def func2():
        n = 30
        print('func2', n)
    func2()

func1()

