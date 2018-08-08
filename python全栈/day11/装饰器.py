#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 装饰器形成的过程
# 装饰器的作用
# 装饰器的原则：开放封闭原则
# 装饰器的固定模式

def wrapper(f):
    def inner(*args, **kwargs):
        '''被装饰函数之前要做的事'''
        ret = f(*args, **kwargs)
        '''被装饰的函数之后要做的事'''
        return ret

    return inner


@wrapper
def func():
    print('老板好')


if __name__ == '__main__':
    func()


# 原则： 开放封闭原则
# 开放： 对扩展是开放的
# 封闭： 对修改是封闭的
# 封版


def garden(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret

    return inner
