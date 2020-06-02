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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebView:

    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "uiautomator2"
        caps["chromedriverExecutable"] = "C:/Users/Yong/PycharmProjects/HogwartsSDET11/ex_appium/driver/chromedriver2.20.exe"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待
        self.driver.implicitly_wait(20)
        #
        # try:
        #     self.driver.find_element(By.XPATH, "//*[@text='同意']").click()
        # finally:
        #     pass

    #  webview  测试
    def test_webview_native(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        submit = (MobileBy.ACCESSIBILITY_ID, "立即开户")
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(submit))
        # 不能输入
        self.driver.find_element(By.XPATH, "//*[@content-desc='平安证券 极速开户'/View[3]/EditText/EditText").send_keys("123456789")

    def test_webview_hybrid(self):
        # scrcpy 更好的录屏工具
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        # for i in range(5):
        #     print(self.driver.contexts)  # 找上下文 看上下文如何切换的
        #     sleep(0.5)
        """  
        #  ['NATIVE_APP', 'WEBVIEW_com.xueqiu.android']
        # 如果有webView 元素 会出现 WEBVIEW_加包名字
        """

        # print(self.driver.page_source)  # NATIVE XML 资源
        # contexts 里面有2个 资源 NATIVE 和 WEBVIEW
        # web_view = self.driver.contexts.last  官方实例 如果有延迟可能切换到自己
        # self.driver.switch_to.context(web_view)
        web_view = self.driver.contexts
        # ['NATIVE_APP', 'WEBVIEW_com.xueqiu.android']
        # 等待webview 资源出现
        # TODO(luoluo_mark_one) ： 再此需要一个隐试等待 webview 资源加载比较慢
        WebDriverWait(self.driver, 10).until(lambda x: len(web_view) > 1)
        # TODO(luoluo_mark_two) ： chromedriver 版本不对应 可以配置 appium mapping file
        self.driver.switch_to.context(web_view[-1])  # 切换到  'WEBVIEW_com.xueqiu.android'
        # 下面和 Chromedriver 交互
        # 2020-03-22 22:35:20:085 [Chromedriver] Set chromedriver binary as:
        # C:/Users/Yong/PycharmProjects/HogwartsSDET11/ex_appium/driver/chromedriver2.20.exe
        # print(self.driver.page_source)  # webView html 资源
        before_window = self.driver.window_handles
        # print('before')
        # print(before_window)
        # TODO(luoluo_mark_three) ： 需要代理 环境 android 6.0 + chrome 62
        self.driver.find_element(By.CLASS_NAME, "trade_home_info_3aI").click()
        # 发送请求以后被代理到8000 端口处理
        # 2020-03-22 22:35:21:460 [WD Proxy] Proxying [POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element]
        # to [POST http://127.0.0.1:8000/wd/hub/session/e137715c543a70f6d1b92222e9dbc34a/element] with
        # body: {"using":"class name","value":"trade_home_info_3aI"}
        after_window = self.driver.window_handles
        # print('after')
        # print(after_window)
        # 等到新的窗口出现
        # TODO(luoluo_mark_four) ： 点击以后打开新的窗口
        WebDriverWait(self.driver, 10).until(lambda x: len(after_window) > len(before_window))
        self.driver.switch_to.window(after_window[-1])
        phone_number = (By.ID, "phone-number")
        # TODO(luoluo_mark_five) ： 元素延时需要隐试等待
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(phone_number))
        self.driver.find_element(*phone_number).send_keys("123456")
        # 切换回到 native 模式
        self.driver.switch_to.context(self.driver.contexts.first)

    def test_webview_work(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        # TODO(luoluo_mark_one) ： 再此需要一个隐试等待 webview 资源加载比较慢
        # 没有测试版的app  先用安卓6
        web_view = self.driver.contexts
        WebDriverWait(self.driver, 10).until(lambda x: len(web_view) > 1)
        # TODO(luoluo_mark_two) ：切换 WEBVIEW_com.xueqiu.android   html 资源
        self.driver.switch_to.context(web_view[-1])
        before_window = self.driver.window_handles
        # TODO(luoluo_mark_three) ： 需要代理 环境 android 6.0 + chrome 62
        self.driver.find_element(By.CLASS_NAME, "trade_home_xueying_SJY").click()
        # 发送请求以后被代理到8000 端口处理
        # 2020-03-22 22:35:21:460 [WD Proxy] Proxying [POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element]
        # to [POST http://127.0.0.1:8000/wd/hub/session/e137715c543a70f6d1b92222e9dbc34a/element] with
        # body: {"using":"class name","value":"trade_home_info_3aI"}
        after_window = self.driver.window_handles
        # print('after')
        # print(after_window)
        # 等到新的窗口出现
        # TODO(luoluo_mark_four) ： 点击以后打开新的窗口
        WebDriverWait(self.driver, 10).until(lambda x: len(after_window) > len(before_window))
        self.driver.switch_to.window(after_window[-1])
        phone_number = (By.CLASS_NAME, "open_form_15N")
        # TODO(luoluo_mark_five) ： 元素延时需要隐试等待
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(phone_number))
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(phone_number))
        user_input = (By.XPATH, '//input[@placeholder="请输入手机号"]')
        self.driver.find_element(*user_input).send_keys("18966903657")
        # user_code_btn = (By.XPATH, "//*[@class='open_input-wrapper_13S']/button")
        user_code_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/button')
        self.driver.find_element(*user_code_btn).click()
        user_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
        self.driver.find_element(*user_code).send_keys("123456")
        sub_but = (By.CSS_SELECTOR, '.open_form-submit_1Ms')
        self.driver.find_element(*sub_but).click()
        toast_alert = (By.CLASS_NAME, 'Toast_toast_22U')
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(toast_alert))
        toast = self.driver.find_element(*toast_alert).text
        assert '请输入正确的验证码' in toast
        # 切换回到 native 模式
        self.driver.switch_to.context(web_view[0])
        self.driver.find_element(By.ID, 'action_bar_close').click()

    """
    获取系统资源占用情况
    执行ADB 命令
    """
    def test_performance(self):

        for p in self.driver.get_performance_data_types():
            print(p)
            print(self.driver.get_performance_data("com.xueqiu.android", p, 10))
        # print(self.driver.get_performance_data("com.xueqiu.android", "cpuinfo", 30))
        # 实际执行的是 adb shell dumpsys cpuinfo
        # 直接执行ABD命令

    def test_shell(self):
        # self.driver.execute_script("mobile: scroll", {'direction': 'down'})
        # 执行此命令时服务端要开启 --relaxed-security
        result = self.driver.execute_script("mobile: shell", {
            'command': 'echo',
            'args': ['arg1', 'arg2'],
            'includeStderr': True,
            'timeout': 5000
        })
        print(result)
        result = self.driver.execute_script("mobile: shell", {
            'command': 'ps',
            'args': [],
            'includeStderr': True,
            'timeout': 5000
        })
        print(result)

    # 查找相同文件
    def teardown(self):
        sleep(10)
        # 学习阶段 先不用退出
        self.driver.quit()


