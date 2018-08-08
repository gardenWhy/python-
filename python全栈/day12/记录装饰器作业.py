#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from functools import wraps
def log(func):
    @wraps(1)
    def inner(*args, **kwargs):
        with open('log', 'a', encoding='utf-8') as f:
            f.write(func.__name__+'\n')
        ret = func(*args, **kwargs)
        return ret

    return inner


@log
def chinese():
    print('进入国内专区')

chinese()