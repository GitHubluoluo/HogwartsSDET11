#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:32 
@Author : Yong
@File : test_profile
@Software: PyCharm
"""

from ex_app_page_object.page.app import App


class TestStocks:

    def setup(self):
        self.stocks = App().start().main().goto_stocks()

    def test_search(self):
        jd = '京东'
        assert jd in self.stocks.search_btn().search('京东').add_select().check()


