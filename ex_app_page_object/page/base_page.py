#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/30 15:30 
@Author : Yong
@File : base_page
@Software: PyCharm
"""
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver = WebDriver
    # 传递参数用
    params = {}

    """
    黑名单
    """
    _black_list = [
        (By.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.XPATH, '//*[@text="下次再说"]'),
        (By.ID, 'ib_close'),
        (By.ID, 'image_cancel')
    ]

    _error_max = 3
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # TODO: 排除弹框，广告，评价异常处理 最好用装饰器 自动处理异常
    def find(self, locator, value=None):
        logging.info(logging)
        logging.info(value)
        try:
            element_ = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            if element_ is not None:
                # 如果成功 清零
                self._error_count = 0
            return element_
        except Exception as e:
            # 错误次数太多 抛出异常
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 递归在找
                    return self.find(locator, value)
            # 如果黑名单没有，就报错
            logging.warning('element not find.')
            raise e

    def find_by_text(self, key):
        return self.find(By.XPATH, "//*[@text='%s']" % key)

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text

    """

    # 数据驱动部分
    
    """

    def steps_driver(self, path):
        # TODO: OPEN 可以打开 url  如果动作存在数据库 使用微服务请求数据返回 yaml 格式数据
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step['action']
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text()
                    elif action in ["input", "send"]:
                        content: str = step['value']
                        for key in self.params.keys():
                            # 替换数据
                            content = str(content).replace("{%s}" % key, self.params[key])
                        element.send_keys(content)
                    elif action == "attribute":
                        element.get_attribute(step["value"])
