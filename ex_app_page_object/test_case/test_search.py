#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:32 
@Author : Yong
@File : test_search
@Software: PyCharm
"""
import pytest
import yaml

from ex_app_page_object.page.app import App


class TestSearch:

    def setup(self):
        self.main = App().start().main().goto_search()

    def test_search(self):
        assert self.main.search("alibaba").get_price("BABA") > 200

    def test_select(self):
        assert "已添加" in self.main.search("JD").add_select().get_add_select()

    # @pytest.mark.parametrize("key, stock_type, price", [
    #     ('alibaba', 'BABA', 200),
    #     ('JD', 'JD', 20)
    # ])
    # TODO: 一 测试数据局驱动 1.方法定义在基类里面BaseTestData类   2.页面测试数据拆分
    @pytest.mark.parametrize("key, stock_type, price", yaml.safe_load(open("data_driver.yaml")))
    def test_search_all(self, key, stock_type, price):
        """
        pytest 装饰器数据参数化
        Args:
            key:
            stock_type:
            price:

        Returns:

        """
        assert self.main.search(key).get_price(stock_type) > price
