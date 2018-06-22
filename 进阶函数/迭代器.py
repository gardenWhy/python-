#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from collections import Iterable,Iterator
print(isinstance('a', Iterable))
print(isinstance('a', Iterator))
# 这些可以直接作用于for循环的对象统称为可迭代对象：Interable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Interator

# 生成器都是Iterator对象，但list、dict、str等是Interable但，不是Iterator
