#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/14 10:00 
@Author : Yong
@File : appium_doc.py 
@Software: PyCharm
"""
# 打开投屏 工具
# http://zuimeia.com/app/6771/?platform=2
"""
Ps: scrcpy --max-size 1080 -T
1. 限制分辨率：
scrcpy --max-size 1024
调整码率：

2.默认码率是 8M，码率越高，画质越好，同时延迟越大，可自行调整：
scrcpy --bit-rate 2M
scrcpy -b 2M  # 简短一点的命令，效果相同
3.录屏：
分为两种情况，一种是投屏状态下录屏：
scrcpy --record file.mp4
scrcpy -r file.mkv
一种是非投屏状态下录屏：
scrcpy --no-display --record file.mp4
scrcpy -Nr file.mkv

4. 多设备连接的情况：
如果有多个设备同时连接电脑，
需要按照前面获取的 ID 号来操作打开 scrcpy：
scrcpy --serial 0123456789abcdef
scrcpy -s 0123456789abcdef

5.窗口置顶：
如果你想要电脑上的手机界面置顶在最上层，
方便在进行其他操作时也可以看到手机画面，可以尝试这个命令：
scrcpy --always-on-top
scrcpy -T

6.关闭手机屏幕：
投屏操作下关闭手机屏幕，只在电脑上看到手机的亮屏状态，
可以使用快捷键 Ctrl+O，或者尝试以下命令：
scrcpy --turn-screen-off
scrcpy -S

*上面这些命令，都可以组合起来一次性输入，然后会直接以修改好的形式启动 scrcpy。

键盘输入：
投屏状态下，可以在对话框界面，调用手机内的中文输入法后，
直接使用电脑键盘输入。
安装 apk、文件传输：直接拖拽即可。
"""
# 使用 appium servse
"""
运行 appium 使用 -g 参数追加 日志 
$ appium -g 'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log'
[Appium] Welcome to Appium v1.16.0
[Appium] Non-default server args:
[Appium]   logFile: C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log
[Appium] Appium REST http interface listener started on 0.0.0.0:4723

# 查看 appium 日志
# less appium.log | grep Running
查看 分析 adb命令 用途
"""

# 可以使用 控件定位 工具 uiautomatorviewer
# 在sdk  Tools  bin 下面
# Ps： uiautomatorviewer


"""
推荐 第三个 按钮 精简版获取 当前页元素 速度快 
amdroid 的界面是基于xml的 
多使用 id 或者 xpath
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
更多关于xpath 语法请看文档  
https://www.w3school.com.cn/xpath/index.asp

绝对定位 不推荐 路径太长

推荐 相对 定位 

//*[@text='热门']

如果使用 Xpath 不严谨 可以使用  contains函数 辅助 resource-id

//*[@text='推荐' and contains(@resource-id,'title')]
使用AccessibilityId 控件要有
content-desc 属性有值才可以
accessibilityId ：content-desc

不推荐  ：name  无用  class name 也不推荐 


"""


# CAPS
# 文档 https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
"""
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
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
"""

# 常用的 api

"""
find_element().click("")
find_element().send_keys("")
"""

# wait 等待
"""
同 selenium 相同
# 显式等待
self.driver.implicitly_wait(10)
# 隐试等待
agree_btn = (MobileBy.ID, "tv_agree")
WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(agree_btn))
"""

# appium 滑动操作
# appium文档 http://appium.io/docs/en/about-appium/intro/

