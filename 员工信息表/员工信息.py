#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('员工信息表.txt', 'r', encoding='utf-8') as f:
    p = f.read().split('\n')
    for i in p:
        print(i)
