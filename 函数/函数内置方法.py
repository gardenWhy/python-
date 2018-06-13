#!/usr/bin/env python
# -*- coding: utf-8 -*-
globals()
# globals() 函数会以字典类型返回当前位置的全部全局变量。
abs()
# 取绝对值
dict()
# 转换成字典
help()
# 帮助
min()
# 取最小值
max()
# 去最大值
all()
# 判断是True还是False，如果是可循环的数据集合(the iterable)是空(empty)的，就是True
any()
# 如果这个可循环集合里有任何一个是True，就返回True
dir()
# 打印了当前程序里承载的所有变量，
hex()
# 转换成16进制
slice()
# 切片，可以提前定义切片的规则，
divmod()
# 求两个值进去求他的整除，和余数,divmod(10,3)会返回(3,1)
sorted()
# sorted(iterable, /, *, key=None, reverse=False)可以通过这个方法，自定义一些排序的规则
ascii()
# 返回Unicode编码
enumerate()
# enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下表，一般用在for循环当中
eval()
# 可以把一个字符串转成代码来执行,只能处理单行代码，有返回值
exec()
# 可以执行多行代码，和eval()用法一样，但是没有返回值
ord()
# 通过字符串返回ascii码的相应的数字值，
chr()
# 通过数字返回ascii对应的字符
sum()
# 把列表里的值求和
bytearray()
# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
map()
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
filter()
# 过滤附和条件的值，list(filter(lambda x:x>3 [1,2,3,4,5,6])),会返回[4,5,6]
import functools

functools.reduce()
# map(),filter(),reduce()三剑客
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
pow()
# 求多少次方
print()
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# end=''结尾以什么结尾，sep=''以什么为两个字符串拼接，
# file=f,f为一个打开的文件流，可以print内容进这个文件里。
# flush
callable()
# 判断一个函数能不能被调用,可以拿来判断是不是函数
frozenset()
# 冷冻的集合，把一个集合变成不可变的集合
vars()
# 当前所有的变量名和值列出来
locals()
# 打印函数的局部变量
repr()
# 显示一个列表，但是是字符串形式
zip()
# 吧两个列表一一对应组合成元组，
compile()
# 编译代码
complex()
# 变成复数
round(1.1123123, 2)
# 保留几位小数
hash()
# 取哈希值
set()
# 把一个列表变成集合
