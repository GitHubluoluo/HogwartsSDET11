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
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:

    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["undefined"] = "uiautomator2"
        caps["noReset"] = True
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就没有了
        caps["dontStopAppOnReset"] = True
        # 如果进程在不用杀死 测试app
        caps["unicodeKeyboard"] = True  # 输入中文
        caps["resetKeyboard"] = True   # 恢复键盘
        caps["skipServerInstallation"] = True  # 跳过server 测试 框架 安装
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待
        self.driver.implicitly_wait(20)
        # 隐试等待
        # agree_btn = (MobileBy.ID, "tv_agree")
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(agree_btn))

    def test_search(self):

        # 点击同意
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        # MobileBy 会自动补齐前面的 模块名称
        # caps["noReset"] = True

        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el1 = self.driver.find_element_by_xpath("//*[@text='推荐' and contains(@resource-id,'title')]")
        # el1.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_get_price(self):
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就不用再点击了
        # caps["noReset"] = True
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("ali")
        self.driver.find_element(MobileBy.ID, "name").click()
        ali_price = self.driver.find_element(MobileBy.ID, "current_price").text
        assert float(ali_price) > 100

    # appium 滑动操作
    # appium文档 http://appium.io/docs/en/about-appium/intro/
    def test_scroll(self):
        # self.driver.get_window_size()
        mobile = self.driver.get_window_rect()
        """
        Python中一般是一行写完所有代码，如果遇到一行写不完需要换行的情况，有两种方法
        1.在该行代码末尾加上续行符“ \”（即空格+\）：
        test = 'item_one' \
            'item_two' \
            'tem_three'
        输出结果：'item_oneitem_twotem_three'
        2.加上括号，() {}  []中不需要特别加换行符：
        test2 = ('csdn '
            'cssdn')
        输出结果：csdn cssdn
        # touch_action = TouchAction(self.driver)
        # touch_action.long_press(x=mobile['width']*0.5, y=mobile['height']*0.8)
        # touch_action.move_to(x=mobile['width']*0.5, y=mobile['height']*0.2)
        # touch_action.release()
        # touch_action.perform()
        """
        # 滑动10次
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=mobile['width'] * 0.5, y=mobile['height'] * 0.8) \
                .move_to(x=mobile['width'] * 0.5, y=mobile['height'] * 0.2) \
                .release() \
                .perform()

    # 系统级 操作
    def test_devices(self):
        # self.driver.start_activity("com.xueqiu.android", ".view.WelcomeActivityAlias")
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    # 课堂作业 通过祖爷爷 找叔叔
    """
    XPATH
    更多关于xpath 语法请看文档  
    https://www.w3school.com.cn/xpath/index.asp
    实例 https://blog.csdn.net/weixin_30418341/article/details/94961241
    """
    def test_get_ali_hk_price(self):
        # 重置数据 为了速度快 可以打开此项 然后 开始点击的同意就不用再点击了
        # caps["noReset"] = True
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        # stock = "//*[@resource-id='com.xueqiu.android:id/title_container']//*[@text='股票']"
        stock = "//*[contains(@resource-id, 'title_container')]//*[@text='股票']"
        self.driver.find_element(MobileBy.XPATH, stock).click()
        # ele_xpath = "//*[@text='09988']/parent::android.widget.LinearLayout/../../android.widget.LinearLayout[2]"
        # ele_xpath = "//*[@text='09988']/../../../android.widget.LinearLayout[2]/android.widget.TextView[1]"
        ele_xpath = "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]"

        ali_price = self.driver.find_element(MobileBy.XPATH, ele_xpath).text
        print(ali_price)
        assert float(ali_price) > 100

    # UiAutomator Selector
    # 滚动到 某个元素
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
    """

    def test_ui_selector(self):

        """
        UiScrollable 如果某个控件可以滚动 定位到控件 
        控件的scrollable(true)属性为真
        调用视图方法 scrollIntoView 传入元素
        UiSelector 定位元素的方法
        """
        sel_str = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("1小时前").instance(0));'
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR, sel_str)
        self.driver.find_element(*scroll_to_element).click()

    # 获取当前 页面资源
    def test_page_source(self):
        # 获取当前页资源
        xml = self.driver.page_source
        # todo：添加一个写入文件的功能
        self.log_xml(xml)

    # 写入文档
    def log_xml(self, page_xlm):
        now = datetime.now()
        with open(now.strftime('H%M%S')+'.xml', 'a') as f:
            f.write(page_xlm)

    # 查找相同文件
    def teardown(self):
        sleep(10)
        # 学习阶段 先不用退出
        self.driver.quit()


