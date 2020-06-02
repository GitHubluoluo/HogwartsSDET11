#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:31 
@Author : Yong
@File : main
@Software: PyCharm
"""
from ex_app_page_object.page.base_page import BasePage
from selenium.webdriver.common.by import By

from ex_app_page_object.page.profile import Profile
from ex_app_page_object.page.search import Search
from ex_app_page_object.page.stocks import Stocks


class Main(BasePage):

    """
    主页功能
    根据业务逻辑 能进入各个子页面
    消息等

    """
    def bottom_nav(self, cont):
        self.find(By.XPATH, "//*[@text='%s' and contains(@resource-id,'tab_name')]" % cont).click()

    def goto_search(self):

        self.find(By.ID, "tv_search").click()
        # self.steps_driver('/steps_driver.yaml')
        return Search(self._driver)

    def goto_stocks(self):
        self.bottom_nav('行情')
        return Stocks(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        self.bottom_nav('我的')
        return Profile(self._driver)

    def goto_massage(self):
        pass

