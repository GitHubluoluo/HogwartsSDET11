#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/3 21:15 
@Author : Yong
@File : test_hogwarts.py.py 
@Software: PyCharm
"""
import os
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwartsOne:

    def setup_method(self):

        # 可以根据配置文件 选择 驱动
        # $ browser = firefox pythes -m ex_selenium/test_*
        # browser = os.getenv("browser", '').lower()
        # if browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # else:
        #     self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome()
        """
        :return:
        无UI模式测试
        https://developers.google.com/web/updates/2017/04/headless-chrome
        # 老版本添加参数
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1280,1696")
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        或者使用
        self.driver = webdriver.Chrome(options={})
        """
        # 新版本添加参数
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=1280,1696")
        # chrome_options.add_argument("--disable-gpu")  # gup 加速

        # 在指定浏览器窗口打开案例 运行共享session
        # 命令行打开浏览器 浏览器安装目录
        # Ps: chrome.exe --remote-debugging-port=9222
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.set_window_size(1936, 1056)
        # self.driver.maximize_window()
        # self.driver.minimize_window()
        # self.driver.get("https://testerhome.com/")
        # 隐试等待 5秒
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    # 显式等待
    def test_hogwarts(self):
        """
        Selenium WebDriver提供了两类waits- 隐式和显式。
        显式的waits会让WebDriver在更深一步的执行前等待一个确定的条件触发，
        隐式的waits则会让WebDriver试图定位元素的时候对DOM进行指定次数的轮询。
        :return:
        """
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.LINK_TEXT, '2020年 第一季度招聘贴').click()
        element = (By.CSS_SELECTOR, '[data-toggle="dropdown"]')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.ID, '华南地区').click()

    # 有iframe 使用frame api 切换
    def test_work_two(self):
        self.driver.get("https://testerhome.com/topics/21495")
        element = (By.CSS_SELECTOR, ".published-form__submit")
        self.driver.switch_to.frame(0)
        """ 
        Usage:
            river.switch_to.frame('frame_name')
            river.switch_to.frame(1)
            river.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        """
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    # 多窗口跳转
    def test_more_window(self):
        self.driver.maximize_window()
        self.driver.get("https://testerhome.com/topics/21805")
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, '第六届中国互联网测试开发大会')
        element.click()
        target_window = element.get_attribute("target")
        if target_window == '_blank':
            chrome_window = self.driver.window_handles
            # 获取所有窗口 跳转
            self.driver.switch_to.window(chrome_window[1])
            # 截图
            self.driver.save_screenshot(chrome_window[1] + ".png")
        link_item = (By.PARTIAL_LINK_TEXT, '演讲申请')
        self.wait(10, expected_conditions.element_to_be_clickable(link_item))
        self.driver.find_element(*link_item).click()
        # 获取所有的窗口
        chrome_window = self.driver.window_handles
        print(chrome_window)

    def test_qw_add_user(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, '添加成员').click()
        # todo: 添加显式等待 确认元素 加载在点击 如果显式等待没有生效可以 循环点击
        WebDriverWait(self.driver, 10).until(self.wait_element)
        self.driver.find_element(By.ID, "username").send_keys("刘强东")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("京东")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("qw_jd_one")
        self.driver.find_element(By.CSS_SELECTOR, ".member_edit_sec:nth-child(1) .ww_label:nth-child(2)").click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("18500000001")
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys("010-80081001")
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("mail001@qq.com")
        self.driver.find_element(By.ID, "memberEdit_address").send_keys("北京大兴亦庄")
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("测试开发")
        self.driver.find_element(By.CSS_SELECTOR, ".member_edit_sec:nth-child(1) .ww_label:nth-child(1)").click()
        self.driver.find_element(By.CLASS_NAME, "js_btn_save").click()
        self.wait(10, expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'js_operationBar_footer')))
        assert "刘强东" in self.driver.page_source
    # 次函数必须有个 参数until要求

    def wait_element(self, e=None):
        # 判断某个元素 出现
        input_size = len(self.driver.find_elements(By.ID, "username"))
        if input_size < 1:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, '添加成员').click()
        return input_size >= 1

    def teardown_method(self):
        sleep(5)
        self.driver.quit()
