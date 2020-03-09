#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/2 20:39 
@Author : Yong
@File : install_EEV.py 
@Software: PyCharm
"""

# Selenium  官网地址
# https://www.selenium.dev/

# Selenium with Python
# https://selenium-python.readthedocs.io/

# 1 selenium 架构
"""
Client:python/java/ruby ->  Selenium ->   Driver:chromeDriver -> Browser:Chrome
"""
# 2 selenium 核心组件

"""
selenium webdriver client   语言客户端
selenium driver   浏览器驱动
selenium IDE     交互式录制案例 工具
selenium gird    集群
"""
# 3 Selenium 组件安装
"""
3.1 安装浏览器    
Chrome  浏览器
3.2 安装selenium driver 
阿里源找 对应浏览器的 驱动 注意版本号
https://npm.taobao.org/mirrors/chromedriver?spm=a2c6h.14029880.0.0.735975d7gR6mlF

解压 放到 浏览器的安装目录 
C:\Users\Yong\AppData\Local\Google\Chrome\Application
https://www.selenium.dev/documentation/zh-cn/webdriver/driver_requirements/
添加环境变量Ps: setx /m path "%path%;C:\Users\Yong\AppData\Local\Google\Chrome\Application"
测试

win  cmd 不完全关闭 可能环境变量不生效 
Ps: chromedriver

Starting ChromeDriver 75.0.3770.8 (681f24ea911fe754973dda2fdc6d2a2e159dd300-refs/branch-heads/3770@{#40}) on port 9515
Only local connections are allowed.

或者  复制一份放入 Anaconda3或者python 下面的 Scripts目录   不建议
C:\ProgramData\Anaconda3\Scripts


3.3 安装selenium-ide
for Chrome 、 for Firefox
https://www.selenium.dev/downloads/

Selenium IDE
Selenium IDE is a Chrome and Firefox plugin which records and plays back user interactions with the browser. 
Use this to either create simple scripts or assist in exploratory testing.
Download latest released version for Chrome or for Firefox or view the Release Notes.
Download previous IDE versions here.

4.用例的关键要素

导入依赖 -> 创建driver ->执行自动化步骤->断言

5. selenium + python 中文文档
https://python-selenium-zh.readthedocs.io/zh_CN/latest/
css 定位符
https://www.w3school.com.cn/cssref/css_selectors.asp 


"""
