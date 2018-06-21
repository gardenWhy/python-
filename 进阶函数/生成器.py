#!/usr/bin/env python
# _*_ coding: utf-8 _*_

a2 = (i for i in range(1000))
print(type(a2))
for i in range(10):
    print(next(a2))
# 生成器只能往前走
# 不能往后取值
# 如果生成器生产到最高，继续生产就会报错StopIteration（停止生产）
