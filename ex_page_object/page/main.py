#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/8 14:41
@Author : Yong
@File : main.py
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from ex_page_object.page.base_page import BasePage
from ex_page_object.page.contacts import Contacts
from ex_page_object.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contacts(self):
        add_member_btn = self.get_element(By.LINK_TEXT, "添加成员")
        # add_member_btn.click()
        # 原生的JS 点击不了可以使用 JS点击 execute_script 语法
        self._driver.execute_script("arguments[0].click();", add_member_btn)
        # 返回Contacts 页面
        return Contacts(self._driver)

    def import_member(self, file_path):
        self.get_element(By.LINK_TEXT, "导入通讯录").click()
        """  
        # 如果不是input 标签上传 
        find input
        js hook execute_script 塞进去值 
        autoit 支持windows 自动化 方案太重  不建议
        cypress 
        """
        self.get_element(By.ID, "js_upload_file_input").send_keys(file_path)
        self.get_element(By.ID, "submit_csv").click()
        self.get_element(By.ID, "reloadContact").click()
        return Contacts(self._driver)

    def goto_message(self):
        self.get_element(By.LINK_TEXT, "消息群发").click()
        return Message(self._driver)
