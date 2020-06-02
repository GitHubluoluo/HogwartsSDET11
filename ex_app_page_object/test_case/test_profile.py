#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:32 
@Author : Yong
@File : test_profile
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from ex_app_page_object.page.app import App


class TestProfile:

    def setup(self):
        self.profile = App().start().main().goto_profile()

    def test_login(self):
        assert '错误' in self.profile.login('18966903657', '123456')

