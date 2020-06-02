#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/14 8:45 
@Author : Yong
@File : test_xueqiu.py 
@Software: PyCharm
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from asyncio import sleep
from datetime import datetime

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:

    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["automationName"] = "uiautomator2"
        # caps["skipServerInstallation"] = True  # 跳过server 测试 框架 安装
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待
        self.driver.implicitly_wait(20)
        # 隐试等待
        # agree_btn = (MobileBy.ID, "tv_agree")
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(agree_btn))

    # 系统弹出框 toast 识别条件
    """
    使用uiautomator2
    automationName: uiautomator2
    getPagesource 无法获取
    必须使用 xpath 查找
    //*[@class='android.widget.Toast']
    //*[contains[@test, 'XXXX']
    """
    def test_api_demo(self):
        loc_text = 'new UiSelector().text("Views")'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, loc_text).click()
        popup_menu = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().description("Popup Menu").instance(0))'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, popup_menu).click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        toast = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        assert 'Search' in toast

    # UiAutomator Selector
    """
    框架 底层 提供 UiAutomator Selector 
    文档 https://developer.android.com/reference/android/support/test/uiautomator/UiSelector.html
    只适用于安卓
    文档 http://appium.io/docs/en/writing-running-appium/android/uiautomator-uiselector/index.html
    事例 https://www.cnblogs.com/cnkemi/p/9185253.html
    1.ID resourceId
        loc_id = 'new UiSelector().resourceId("com.baidu.yuedu:id/webbooktitle")'
        driver.find_element_by_android_uiautomator(loc_id).click()
    2.文本 text
        loc_text = 'new UiSelector().text("图书")'
        driver.find_element_by_android_uiautomator(loc_text).click()
    3.类 className复数定位
        loc_class = 'new UiSelector().className("android.widget.TextView")'
        driver.find_elements_by_android_uiautomator(loc_class)[2].click()
    4.description 也是用contenet-des属性定位
        new UiSelector().description("contenet-des属性")
    5.组合定位
        1).id与text属性组合
            #id+text
            id_text = 'resourceId("com.baidu.yuedu:id/webbooktitle").text("小说")'
            driver.find_element_by_android_uiautomator(id_text).click()
        2).class与text属性组合
            #class+text
            class_text = 'className("android.widget.TextView").text("图书")'
            driver.find_element_by_android_uiautomator(class_text).click()   
             
    uiautomator UiSelector
    Appium 使用 UiSelectors 来进行查找。 同时也支持 UiScrollable。
    
    注意，根据索引查找并不可靠，所以更应该使用实例(instance)。后续的示例是使用 Ruby 来测试 api demos apk。
    查找第一个 textview。
    # ruby
    first_textview = find_element(:uiautomator, 'new UiSelector().className("android.widget.TextView").instance(0)');
    根据文本查找第一个元素。
    # ruby
    first_text = find_element(:uiautomator, 'new UiSelector().text("Animation")')
    first_text.text # "Animation"
    查找第一个可滚动(scrollable)的元素，然后根据文本"Tabs"查找第一个 TextView。 "Tabs"元素将被滚动到可见范围。
    # ruby
    element = find_element(:uiautomator, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Tabs")')
    作为一个特例，scrollIntoView 返回的是被滚动到可见范围的元素。 scrollIntoView 允许滚动到任意的 UiSelector。
    # ruby
    element = find_element(:uiautomator, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0));')
    element.text # "WebView"
    本文由 NativeZhang 翻译，由 lihuazhang 校验。             
    """



    # 查找相同文件
    def teardown(self):
        sleep(10)
        # 学习阶段 先不用退出
        self.driver.quit()


