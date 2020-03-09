#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
from ex_hogwarts.sdet.Student import Student
from ex_python import fibo

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


# 四 python 模块与包 默认从当前目录找
# 引入模块
# import fibo
fibo.fib(1000)
# 如果你想经常使用某个函数，你可以把它赋值给一个局部变量:
fib = fibo.fib
fib(500)
# import 语句有一个变体，它可以把名字从一个被调模块内直接导入到现模块的符号表里
# from fibo import fib, fib2
fib(500)
# from fibo import *
fib(500)
# from fibo import fib as fibonacci
# fibonacci(500)

#  引入包 from hogwarts.sdet.Student import Student

"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""

# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)

# from sound.effects import echo
# echo.echofilter(input, output, delay=0.7, atten=4)

s = Student()


# 五 python测试框架 标准库unittest 单元测试框架 了解
# https://docs.python.org/zh-cn/3.7/library/unittest.html
# 1.test fixture  测试预制
# 2 test case 测试用例
# 3 test suite 测试套件 容纳用例
# 4 test runner 运行
"""
为了实现这些，unittest 通过面向对象的方式支持了一些重要的概念。

测试脚手架
test fixture 表示为了开展一项或多项测试所需要进行的准备工作，以及所有相关的清理操作。举个例子，这可能包含创建临时或代理的数据库、目录，再或者启动一个服务器进程。

测试用例
一个测试用例是一个独立的测试单元。它检查输入特定的数据时的响应。 unittest 提供一个基类： TestCase ，用于新建测试用例。

测试套件
test suite 是一系列的测试用例，或测试套件，或两者皆有。它用于归档需要一起执行的测试。

测试运行器（test runner）
test runner 是一个用于执行和输出测试结果的组件。这个运行器可能使用图形接口、文本接口，或返回一个特定的值表示运行测试的结果。
"""

# 六 集成测试框架 Pytest  https://docs.pytest.org/en/latest/



