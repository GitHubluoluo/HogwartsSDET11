#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:32
@Author : Yong
@File : test_search
@Software: PyCharm
"""
import logging

import pytest
import yaml

from ex_app_page_object.page.app import App


class TestDataDriver:

    def setup(self):
        self.main = App().start().main()


    # 1 .数据驱动
    # @pytest.mark.parametrize("key, stock_type, price", [
    #     ('alibaba', 'BABA', 200),
    #     ('JD', 'JD', 20)
    # ])
    # TODO: 一 测试数据局驱动 1.方法定义在基类里面BaseTestData类   2.页面测试数据拆分
    @pytest.mark.parametrize("key, stock_type, price", yaml.safe_load(open("data_driver.yaml")))
    def test_data_driver(self, key, stock_type, price):
        """
        pytest 装饰器数据参数化
        Args:
            key:
            stock_type:
            price:

        Returns:

        """
        assert self.main.goto_search().search(key).get_price(stock_type) > price

    # 2.步骤驱动
    # TODO: 2.如果是开发的测试平台需要，项目测试 PO完全满足
    #  常规项目不建议使用步骤驱动 维护成本高 鸡肋
    # 步骤文件 可以根据路径 文件名或者方法名查找

    def test_steps_driver(self, key=None):
        key = 'alibaba'
        # 传递参数给base类 清空
        self.main.params.clear()
        self.main.params['key'] = key
        # goto search
        self.main.steps_driver("../page/steps_driver.yaml")
        # search
        self.main.steps_driver("../page/search_driver.yaml")


