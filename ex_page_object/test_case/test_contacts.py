#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/6 20:24 
@Author : Yong
@File : test_contacts.py
@Software: PyCharm
"""
from ex_page_object.page.contacts import Contacts


class TestContacts:

    def setup(self):
        # 初始化  Page
        self.contacts = Contacts()

    def test_edit_member(self):
        self.contacts.edit_member("刘强东", {"mobile": "18500617362"}).get_success("保存成功")

    def teardown(self):
        self.contacts.close()
