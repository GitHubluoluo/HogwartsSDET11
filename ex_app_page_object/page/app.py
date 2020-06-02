#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from ex_app_page_object.page.base_page import BasePage
from ex_app_page_object.page.main import Main


"""
@Time : 2020/5/30 15:29 
@Author : Yong
@File : app
@Software: PyCharm
"""


class App(BasePage):


    """
    代表雪球app的基础业务行为的功能
    启动 start
    重启 restart
    停止 stop
    强制退出 kill 进程
    后台运行 等功能

    进入主页PO的功能 main

    """
    def start(self):
        """
        app
        入口
        """
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"

        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "xiaomi"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["automationName"] = "uiautomator2"
            caps["chromedriverExecutable"] = "C:/Users/Yong/PycharmProjects/HogwartsSDET11/ex_appium/driver/chromedriver2.20.exe"
            # caps["noReset"] = True 重置数据
            # caps["dontStopAppOnReset"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 显式等待
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        """
        进入主页
        Returns:
        """
        def wait_load(driver):
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            return False
        WebDriverWait(self._driver, 30).until(wait_load)
        # WebDriverWait(self._driver, 30).until(lambda x: '我的' or '同意' in self._driver.page_source)
        # TODO: wait main page id ib_close
        return Main(self._driver)

