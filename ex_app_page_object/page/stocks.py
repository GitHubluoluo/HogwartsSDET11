#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:31 
@Author : Yong
@File : search
@Software: PyCharm
"""


from selenium.webdriver.common.by import By
from ex_app_page_object.page.search import Search


class Stocks(Search):

    """
    复用 搜索功能
    根据类型选择股票
    断言股价
    加自选

    """

    def search_btn(self):
        self.find(By.ID, "action_search").click()
        return self

    def check(self):
        self.find(By.ID, "action_close").click()
        # self.find(By.ID, "title_text").click()
        return self._driver.page_source
