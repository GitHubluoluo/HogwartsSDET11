#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/14 8:45 
@Author : Yong
@File : test_xueqiu.py 
@Software: PyCharm
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from asyncio import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueqiu:

    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["undefined"] = "uiautomator2"
        # caps["noReset"] = True
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就没有了

        caps["unicodeKeyboard"] = True  # 输入中文
        caps["resetKeyboard"] = True   # 恢复键盘
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_search(self):

        # 点击同意
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        # MobileBy 会自动补齐前面的 模块名称
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el1 = self.driver.find_element_by_xpath("//*[@text='推荐' and contains(@resource-id,'title')]")
        # el1.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_get_price(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        price = self.driver.find_element(MobileBy.ID, "current_price").text()
        assert float(price) > 100

    def teardown(self):
        sleep(20)
        self.driver.quit()


