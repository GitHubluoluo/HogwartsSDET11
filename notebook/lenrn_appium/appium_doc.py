#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/14 10:00 
@Author : Yong
@File : appium_doc.py 
@Software: PyCharm
"""
# 打开投屏 工具
"""
Ps: scrcpy 

"""
# 使用 appium servse
"""
运行 appium 使用 -g 参数追加 日志 
$ appium -g 'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log'
[Appium] Welcome to Appium v1.16.0
[Appium] Non-default server args:
[Appium]   logFile: C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
"""
# 借助appium desktop

"""
# 查看 app 控件的定位

打开 appium desktop -> 点击 start inspector session (端口号换 5723)-> 选择 custom server 

# 测试参数 
{
  "platformName": "android",
  "deviceName": "xiaomi",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "undefined": "uiautomator2"
}

amdroid 的界面是基于xml的 
多 使用 id 或者 xpath
Attribute   Value
elementId	9a90367c-5b6e-4723-9e96-1c5b39068034
index	0
package	com.xueqiu.android
class	android.widget.TextView
text	热门
resource-id	com.xueqiu.android:id/title_text
checkable	false


ID
resource-id	com.xueqiu.android:id/title_text
使用 title_text 找到 3个

XPATH
更多关于xpath 语法请看文档  https://www.w3school.com.cn/xpath/index.asp

绝对定位 不推荐 路径太长

推荐 相对 定位 

//*[@text='热门']

如果使用 Xpath 不严谨 可以使用  contains函数 辅助 resource-id

//*[@text='推荐' and contains(@resource-id,'title')]
使用AccessibilityId 控件要有
content-desc 属性有值才可以
accessibilityId ：content-desc

不推荐  ：name  无用  class name 也不推荐 


ios 

多使用 content-desc 属性 accessfor 定位

"""
# 常用的 api

"""
find_element().click("")
find_element().send_keys("")
"""


# 可以使用 控件定位 工具 uiautomatorviewer
# 在sdk  Tools  bin 下面
# Ps： uiautomatorviewer
"""
推荐 第三个 按钮 精简版获取 当前页元素 速度快 
"""
