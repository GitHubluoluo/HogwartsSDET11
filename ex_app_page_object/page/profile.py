#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:31 
@Author : Yong
@File : profile
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from ex_app_page_object.page.base_page import BasePage


class Profile(BasePage):

    def login(self, key, password):
        self.find(By.XPATH, "//*[@text='帐号密码登录']").click()
        self.find(By.ID, "login_account").send_keys(key)
        self.find(By.ID, "login_password").send_keys(password)
        self.find(By.ID, "button_next").click()
        # webwiew toast 弹框
        # self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
        msg = self.text
        self.find(By.ID, 'md_buttonDefaultPositive')
        return msg
