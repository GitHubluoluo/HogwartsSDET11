#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/6 20:24 
@Author : Yong
@File : index.py 
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from ex_page_object.page.base_page import BasePage
from ex_page_object.page.login import Login
from ex_page_object.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com"

    def goto_register(self):
        self.get_element(By.LINK_TEXT, "立即注册").click()
        # 返回register 页面
        return Register(self._driver)

    def goto_login(self):
        self.get_element(By.LINK_TEXT, "企业登录").click()
        return Login(self._driver)

    def add_contacts(self):
        pass
