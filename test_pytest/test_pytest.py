#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# content of test_pytest.py
"""
文件范围
test_*.py 或者 *_test.py
用例识别
test 类之外的带前缀test_*测试功能或方法
test前缀测试Test*类中的前缀test_*测试函数或方法(类中无__init__方法)
兼容 unittest
"""

import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


"""
以“安静”报告模式执行测试功能：
$ pytest -q test_sysexit.py
1 passed in 0.12s
"""


#  开发多个测试后，您可能需要将它们分组到一个类中。pytest使创建包含多个测试的类变得容易：


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


# 测试用例的执行顺序
"""
setup_module
@class_method
setup_method
setup_function
teardowen_*
pytest-order
"""


def setup_module():
    print("setup_module")


def setup_function():
    print("setup_function")


class TestMyClass:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
