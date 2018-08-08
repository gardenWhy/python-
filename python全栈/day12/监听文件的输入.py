#!/usr/bin/env python
# _*_ coding: utf-8 _*_
def tail(filename):
    f = open(filename,encoding='utf-8')
    while True:
        line = f.readline()
        if line.split():
            yield line.split()

g = tail('file')
for i in g:
    print(i)