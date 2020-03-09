#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/3 21:15 
@Author : Yong
@File : test_hogwarts.py.py 
@Software: PyCharm
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from ex_selenium.test_work_two import TestHogwartsOne

class TestWorkThree(TestHogwartsOne):

    def test_work_browser(self):
        # 使用火狐浏览器
        # self.driver = webdriver.Firefox()
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '第六届中国互联网测试开发大会').click()
        # 获取所有窗口跳转
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        element = (By.LINK_TEXT, '演讲申请')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    # 执行JS
    def test_java_script(self):
        self.driver.get("https://testerhome.com/")
        # todo 专项测试的时候讲解获取性能
        for code in [
            "return document.title",
            "return document.querySelector('.active').className",
            "return JSON.stringify(performance.timing)"
        ]:
            result = self.driver.execute_script(code)
            print(result)




