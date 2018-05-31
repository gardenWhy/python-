#!/usr/bin/env python
# -*- coding: utf-8 -*-
age = 19
def func1():
    global age
    def func2():
        print(age)
    age = 73
    func2()

func1()
print(age)