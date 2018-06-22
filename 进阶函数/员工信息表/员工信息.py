#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1、可以支持以下搜索语法
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT" //dept：部门
find * from staff_table were enroll_data like "2013" //enroll_data：入职日期

2、可以创建新的员工信息,以Phone做唯一键（即不允许表里有手机号重复的情况）,staff_id需要自增
add staff Alex Li,25,134435344,IT,2015-10-29

3、可以删除指定的员工信息，输入id直接删除
del staff 3

4、可以修改员工信息，
UPDATE staff_table SET dept="Market" WHERE dept="IT" //把所有dept为IT的记录的信息改为Market


'''
with open('员工信息表.txt', 'r', encoding='utf-8') as f:
    p = f.read().split('\n')
    for i in p:
        print(i)
def welcome():
    print('''
    欢迎来到员工信息查询系统！
        操作选项：
        1、查询员工信息
        2、新增员工信息
        3、删除员工信息
        4、修改员工信息 
        5、显示现有员工信息   
        ''')
def search():
    print('''
    -------------------欢迎进入员工信息查询界面-----------------
    ********************************************************
                          命令行示例
    find name,age from staff_table where age > 22
    find * from staff_table where dept = "IT" 
    find * from staff_table were enroll_data like "2013" 
    ********************************************************
    请输入你的查询语句（返回上一层，请输入q）
    ''')

welcome()