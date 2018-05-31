#!/usr/bin/env python
# -*- coding: utf-8 -*-

def send_alert(msg, *users):
    for i in users:
        print('发给' + i)


send_alert('cnm', 'garden', 'why')


def func(name, *args, **kwargs):
    print(name, args, kwargs)


func('garden', 19, 'tesla', '500w', addr='嗯', num='hhh')

d = {'why': 'hhhhh'}
func('ass', **d)
