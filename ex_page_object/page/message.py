#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/8 21:03 
@Author : Yong
@File : tools.py
@Software: PyCharm
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from ex_page_object.page.base_page import BasePage


class Message(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#createMessage"

    def send_msg(self, app, content, group):
        self.get_element(By.CLASS_NAME, "js_select_apps_btn").click()
        self.get_element(By.CSS_SELECTOR, "div[data-name='%s']" % app).click()
        self.get_element(By.CSS_SELECTOR, "a[d_ck='submit']").click()
        self.get_element(By.CLASS_NAME, "js_select_range_btn").click()
        self.get_element(By.ID, "memberSearchInput").send_keys(group)
        self.get_element(By.CSS_SELECTOR, "#searchResult li:nth-child(1)").click()
        self.get_element(By.CSS_SELECTOR, "a[d_ck='submit']").click()
        self.get_element(By.CSS_SELECTOR, "textarea.js_send_msg_text").send_keys(content)
        self.get_element(By.CLASS_NAME, "js_save_send.js_disabled_item").click()
        self.get_element(By.CSS_SELECTOR, "a[node-type='ok']").click()
        return self

    def get_success(self, msg):
        self.wait(10, expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'msg_history_msgList')))
        return msg in self.get_element(By.ID, "js_tips").text

