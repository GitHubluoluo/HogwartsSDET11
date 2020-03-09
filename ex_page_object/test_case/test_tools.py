#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/6 20:24 
@Author : Yong
@File : test_tools.py
@Software: PyCharm
"""

from ex_page_object.page.tools import Tools


class TestMain:

    def setup(self):
        # 初始化  Page
        self.tools = Tools()

    def test_import_member(self):
        path = r'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_page_object\test_case\test.jpg'
        self.tools.import_material_img(path)

    def teardown(self):
        self.tools.close()
