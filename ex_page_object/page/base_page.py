#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/7 15:08 
@Author : Yong
@File : BasePage.py 
@Software: PyCharm
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""
BasePage  
定义 一些和driver 的方法  get_element_id()  或者显式等待 等方法 
Tool  
定义 back_btn  工具类 后退什么的 
"""


class BasePage:

    _base_url = None

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            self._chromeOptions = Options()
            # Ps: chrome.exe --remote-debugging-port=9222
            self._chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            self._driver = webdriver.Chrome(options=self._chromeOptions)
            # self._driver = webdriver.Chrome()
            self._driver.get(self._base_url)
        else:
            self._driver = driver
        self._driver.implicitly_wait(5)

    def close(self):
        sleep(10)
        self._driver.quit()

    def wait(self, timeout, method):
        WebDriverWait(self._driver, timeout).until(method)

    def get_element(self, by, locator):
        return self._driver.find_element(by, locator)

    def get_elements(self, by, locator):
        return self._driver.find_element(by, locator)
