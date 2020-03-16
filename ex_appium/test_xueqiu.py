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
from datetime import datetime

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:

    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["undefined"] = "uiautomator2"
        caps["noReset"] = True
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就没有了
        caps["dontStopAppOnReset"] = True
        # 如果进程在不用杀死 测试app
        caps["unicodeKeyboard"] = True  # 输入中文
        caps["resetKeyboard"] = True   # 恢复键盘
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待
        self.driver.implicitly_wait(10)
        # 隐试等待
        # agree_btn = (MobileBy.ID, "tv_agree")
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(agree_btn))

    def test_search(self):

        # 点击同意
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        # MobileBy 会自动补齐前面的 模块名称
        # caps["noReset"] = True

        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el1 = self.driver.find_element_by_xpath("//*[@text='推荐' and contains(@resource-id,'title')]")
        # el1.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_get_price(self):
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就不用再点击了
        # caps["noReset"] = True
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("ali")
        self.driver.find_element(MobileBy.ID, "name").click()
        ali_price = self.driver.find_element(MobileBy.ID, "current_price").text
        assert float(ali_price) > 100

    def test_scroll(self):
        # self.driver.get_window_size()
        mobile = self.driver.get_window_rect()
        """
        Python中一般是一行写完所有代码，如果遇到一行写不完需要换行的情况，有两种方法
        1.在该行代码末尾加上续行符“ \”（即空格+\）：
        test = 'item_one' \
            'item_two' \
            'tem_three'
        输出结果：'item_oneitem_twotem_three'
        2.加上括号，() {}  []中不需要特别加换行符：
        test2 = ('csdn '
            'cssdn')
        输出结果：csdn cssdn
        # touch_action = TouchAction(self.driver)
        # touch_action.long_press(x=mobile['width']*0.5, y=mobile['height']*0.8)
        # touch_action.move_to(x=mobile['width']*0.5, y=mobile['height']*0.2)
        # touch_action.release()
        # touch_action.perform()
        """
        # 滑动10次
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=mobile['width'] * 0.5, y=mobile['height'] * 0.8) \
                .move_to(x=mobile['width'] * 0.5, y=mobile['height'] * 0.2) \
                .release() \
                .perform()

    # 系统级 操作
    def test_devices(self):
        # self.driver.start_activity("com.xueqiu.android", ".view.WelcomeActivityAlias")
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def test_get_ali_hk_price(self):
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就不用再点击了
        # caps["noReset"] = True
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        ali_price = self.driver.find_element(MobileBy.XPATH, "//*[@text='09988']/../TextView[2]").text
        print(ali_price)
        # assert float(ali_price) > 100

    def test_page_source(self):
        # 获取当前页资源
        xml = self.driver.page_source
        # todo：添加一个写入文件的功能
        self.log_xml(xml)

    def log_xml(self, page_xlm):
        now = datetime.now()
        with open(now.strftime('H%M%S')+'.xml', 'a') as f:
            f.write(page_xlm)

    # 查找相同文件
    def teardown(self):
        sleep(10)
        # 学习阶段 先不用退出
        self.driver.quit()


