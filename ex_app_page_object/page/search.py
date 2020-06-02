#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:31 
@Author : Yong
@File : search
@Software: PyCharm
"""

from selenium.webdriver.common.by import By
from ex_app_page_object.page.base_page import BasePage


class Search(BasePage):

    """
    搜索功能
    根据类型选择股票
    断言股价
    加自选

    """
    # TODO: 多平台，多版本，多可能定位符
    """
    经常需要用的元素 控件 
    根据平台 页面从外部的配置文件获取 
    """
    _name = (By.ID, "name")

    def search(self, key: str):
        """
        # 数据驱动
        # self.main.steps_driver("search_driver.yaml")
        """
        search = (By.ID, "search_input_text")
        self.find(search).send_keys(key)
        self.find(self._name).click()
        return self

    def get_price(self, stock_type: str) -> float:
        return float(self.find(By.ID, "current_price").text)

    def add_select(self):
        self.find_by_text("加自选").click()
        return self

    def un_select(self):
        self.find_by_text("已添加").click()
        return self

    def get_add_select(self):
        return self.find(By.ID, 'followed_btn').text

