#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/3 21:15 
@Author : Yong
@File : test_hogwarts.py.py 
@Software: PyCharm
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1936, 1056)
        self.driver.get("https://testerhome.com/")
        # 隐试等待  默认都加上 3-6s 为了所有的findElement 方法都可以找到
        # self.driver.implicitly_wait(5)

    # 显式等待 处理隐试等待无法解决得出问题 如文件上传
    # 自定义显式等待方法里面有find 会出现冲突 等待6秒 隐试
    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        """
        Selenium WebDriver提供了两类waits- 隐式和显式。
        显式的waits会让WebDriver在更深一步的执行前等待一个确定的条件触发，
        隐式的waits则会让WebDriver试图定位元素的时候对DOM进行指定次数的轮询。
        :return:
        """
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(3)
        # todo : 改进方向 显式等待 写等待时间  客户端在等待
        # down ： 完成
        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        # 显式条件满足
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        # 自定义 显式等待 不推荐
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(element) > 1)
        """
        web资源加载顺序
        title出现
        dom 出现 presence
        css 出现 visibility
        js 执行 clickable
        """
        self.driver.find_element(*element).click()
        # 尽量使用css 定位符 link  比较快可能资源未加载
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()
        # todo ： 隐式等待 一直循环找知道超时  server 在等待

        # self.driver.find_elements(By.CSS_SELECTOR, 'div.topic:nth-child(1) .title > a').click()

    def teardown_method(self):
        sleep(10)
        self.driver.quit()
