#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/6 20:24 
@Author : Yong
@File : test_index.py 
@Software: PyCharm
"""
from ex_page_object.page.index import Index


class TestIndex:

    """
    ① 先把实例 模拟写出来在  测试ok 再优化
    def test_register(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        self.driver.find_element(By.ID, "corp_name").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "submit_btn").click()

    ② 根据需求 拆分 case  提取出来 driver page  test  部分 拆分 2个 page PO

    """

    def setup(self):
        # 初始化 index Page
        self.index = Index()

    def test_register(self):
        # 链式调用
        self.index.goto_register().register("霍格沃兹测试学院")

    def test_login(self):
        register_page = self.index.goto_login().goto_register().register("霍格沃兹测试学院")
        msg_list = register_page.get_error_msg()
        assert "请选择" in ' '.join(msg_list)

    def teardown(self):
        self.index.close()
