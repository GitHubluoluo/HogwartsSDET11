#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/7 21:42 
@Author : Yong
@File : login.py 
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from ex_page_object.page.base_page import BasePage
from ex_page_object.page.register import Register


class Login(BasePage):

    def scan_code(self):
        pass

    def goto_register(self):
        self.get_element(By.LINK_TEXT, "企业注册").click()
        return Register(self._driver)
