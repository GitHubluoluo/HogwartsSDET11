#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/6 20:24 
@Author : Yong
@File : test_main.py
@Software: PyCharm
"""

from ex_page_object.page.main import Main


class TestMain:

    def setup(self):
        # 初始化  Page
        self.main = Main()

    def test_add_member(self):
        # 链式调用
        result = self.main.goto_contacts().add_member().get_success("保存成功")
        assert result is True

    def test_import_member(self):
        path = r'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_page_object\test_case\洛洛通讯录.xlsx'
        self.main.import_member(path)

    def test_send_msg(self):
        result = self.main.goto_message().send_msg(app="一元竞拍", content="竞拍开始了", group="洛洛")
        result.get_success('发送成功')

    def teardown(self):
        self.main.close()

