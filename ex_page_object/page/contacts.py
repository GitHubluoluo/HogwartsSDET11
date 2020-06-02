#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/8 14:41 
@Author : Yong
@File : contacts.py 
@Software: PyCharm
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from ex_page_object.page.base_page import BasePage


class Contacts(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self):
        # 建议使用 By.NAME 因为ID 可能改
        self.get_element(By.NAME,  "username").send_keys("刘强东")
        self.get_element(By.NAME, "english_name").send_keys("京东")
        self.get_element(By.NAME, "acctid").send_keys("qw_jd_one")
        self.get_element(By.CSS_SELECTOR, ".ww_radio[value='1']").click()
        # self.get_element(By.CSS_SELECTOR, ".ww_radio+span:contains('男')")).click()
        self.get_element(By.NAME, "mobile").send_keys("18500000001")
        self.get_element(By.NAME, "ext_tel").send_keys("010-80081001")
        self.get_element(By.NAME, "alias").send_keys("mail001@qq.com")
        self.get_element(By.NAME, "xcx_corp_address").send_keys("北京大兴亦庄")
        self.get_element(By.NAME, "position").send_keys("测试开发")
        self.get_element(By.CSS_SELECTOR, ".member_edit_sec:nth-child(1) .ww_label:nth-child(1)").click()
        self.get_element(By.CLASS_NAME, "js_btn_save").click()
        return self

    def edit_member(self, member, data):
        self.wait(10, expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'js_operationBar_footer')))
        self.get_element(By.CSS_SELECTOR, "td[title=%s]" % member).click()
        self.get_element(By.CSS_SELECTOR, "a.js_edit").click()
        for key, vla in data.items():
            self.get_element(By.CSS_SELECTOR, "input[name=%s]" % key).clear()
            self.get_element(By.CSS_SELECTOR, "input[name=%s]" % key).send_keys(vla)
        self.get_element(By.CSS_SELECTOR, "a.js_save").click()
        return self

    def get_success(self, msg):
        success_tag = (By.ID, 'js_tips')
        self.wait(10, expected_conditions.visibility_of_element_located(success_tag))
        return msg in self.text

