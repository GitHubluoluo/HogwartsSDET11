#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


# 一 、python数据 类型
# 1.数字 https://docs.python.org/3.7/tutorial/introduction.html#numbers
number = 2
print(number)
# 2.字符串
# 使用r 转换为字符串 print('c:\some\name')
print(r'c:\somen\name')
# 多行使用 三个 双引号""" 样式"""
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# 字符串格式化f
x = '你好'
print(f'testHome{x}')
# 3 列表 []
lists = [1, 2, 3, 4, 5, 6]
print(lists[1:3])
print(lists[3:])
print(lists[-1])
print(lists[-2:])
# 3.1列表 堆栈
lists.append('a')
print(lists)
l_p = lists.pop()
print(l_p)
print(lists)
# 3.2列表使用deque()队列
lists = deque(lists)
lists.append('a')
print(lists)
lists.popleft()
print(lists)
new_list = [x*10 for x in range(10)]
print(new_list)
# 4 集合 Sets 无排序 无重复元素
basket = {}
# 5 元祖 Tuples 不可修改
# 6 列表 Lists 可修改
# 7 字典 Dictionaries 关系数据

# 二、python数据 类型
# 8 函数


def fun(a, b=1, *c, **d):
    """
    :param a:  为必填参数 fun(a)
    :param b:  默认值
    :param c:  元组
    :param d:  字典
    :return:
    """
    print(f'a={a}\nb={b}\nc={c}\nd={d}')


# a 为必填参数
print('-'*10+'必填'+'-'*10)
fun('apple')
"""
a=apple
b=1
c=()
d={}
"""
print('-'*10+'默认值'+'-'*10)
fun('banana', 2)
"""
a=banana
b=2
c=()
d={}
"""
print('-'*10+'元组'+'-'*10)
fun('pear', 5, 'php', 'java', 'js')
"""
a=pear
b=5
c=('php', 'java', 'js')
d={}
"""
print('-'*10+'字典'+'-'*10)
fun('pear', 5, 'php', 'java', 'js', x=1, y=2, z=3)
"""
a=pear
b=5
c=('php', 'java', 'js')
d={'x': 1, 'y': 2, 'z': 3}
"""

# 9 解包参数列表
lists1 = list(range(3, 6))
print(lists1)
"""
[3, 4, 5]
"""
args = [3, 6]
lists2 = list(range(*args))  # 传参使用*解包
print(lists2)
"""
[3, 4, 5]
"""
# 10 Lambda 表达式 创建匿名函数


def make_incrementor(n):
    """
    :param n:
    :return:
    """
    return lambda x: x + n


f = make_incrementor(0)
print(f(1))
print(f(5))
"""
1
5
"""

# 11 函数标注 以字典的形式存放在函数的 __annotations__ 属性中
# 标注函数 参数 和 返回值类型


def f(ham: str, eggs: str = 'eggs') -> str:
    """
    :param ham:
    :param eggs:
    :return: str
    """
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


print(f('spam'))

"""
Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
spam and eggs
"""

#  三、 类与方法
# 12 普通类 变量与类方法


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
print(x.i)
print(x.f())

# 13  实例化运算符的参数将被传递给 __init__()


class Complex:

    def __init__(self, realpart, imagpart):
        """
        :param realpart:
        :param imagpart:
        """
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x)


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    def name(self):
        print(self.name)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

"""
d.tricks
['roll over']
e.tricks
['play dead']
"""
# 14 类的方法


class Teacher:
    @classmethod
    def share(cls, *c):
        print(c)


Teacher.share(1, 2, 3,)


# python 的包与模块

