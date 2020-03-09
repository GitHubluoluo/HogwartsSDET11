#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


"""
通过 setUp() 和 tearDown() 方法，可以设置测试开始前与完成后需要执行的指令，测试框架会自动地为每个单独测试调用前置方法。
在测试运行时，若 setUp() 方法引发异常，测试框架会认为测试发生了错误，因此测试方法不会被运行。
相似的，我们提供了一个 tearDown() 方法在测试方法运行后进行清理工作。
若 setUp() 成功运行，无论测试方法是否成功，都会运行 tearDown() 

unittest 模块可以通过命令行运行模块、类和独立测试方法的测试:

python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
你可以传入模块名、类或方法名或他们的任意组合。

同样的，测试模块可以通过文件路径指定:

python -m unittest tests/test_something.py
"""


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
