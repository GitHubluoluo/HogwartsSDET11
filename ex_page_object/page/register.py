#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/7 16:05 
@Author : Yong
@File : Register.py 
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from ex_page_object.page.base_page import BasePage


class Register(BasePage):

    def register(self, company):
        self.get_element(By.ID, "corp_name").send_keys(company)
        self.get_element(By.ID, "submit_btn").click()
        return self

    def get_error_msg(self):
        msgs = self.get_element(By.CLASS_NAME, ".js_error_msg")
        msg_list = []
        for msg in msgs:
            msg_list.append(msg.text)
        return msg_list
