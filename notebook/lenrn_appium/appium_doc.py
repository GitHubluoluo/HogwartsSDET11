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

# 定位
# 事例 https://blog.csdn.net/ouyanggengcheng/article/details/88558224
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
实例 https://blog.csdn.net/weixin_30418341/article/details/94961241

框架 底层 提供 UiAutomator Selector 
文档 https://developer.android.com/reference/android/support/test/uiautomator/UiSelector.html
只适用于安卓
官方 实例1  http://appium.io/docs/en/writing-running-appium/android/uiautomator-uiselector/index.html

实例2  https://www.cnblogs.com/cnkemi/p/9185253.html
元素定位方式有多种，Android也有自身独有的定位方式。下面就单独介绍其基于uiautomator定位元素的方法：
基本语法：
driver.find_element_by_android_uiautomator(xx)
1.文本定位
    1).通过text文本定位语法
    new UiSelector().text("text文本")
    #text
    loc_text = 'new UiSelector().text("图书")'
    driver.find_element_by_android_uiautomator(loc_text).click()
    2).如果文本比较长，可以用textContains模糊匹配
    new UiSelector().textContains("包含text文本")
    # textContains
    loc_textContains = 'new UiSelector().textContains("图")'
    driver.find_element_by_android_uiautomator(loc_textContains).click()
    3).同样可以用textStartsWith是以某个文本开头来匹配
    new UiSelector().textStartsWith("以text文本开头")
    #textStartsWith
    loc_textStart = 'new UiSelector().textStartsWith("图")'
    driver.find_element_by_android_uiautomator(loc_textStart).click()
    4).也可以用正则表达式textMatches匹配
    new UiSelector().textMatches("正则表达式")
2.resourceId 与by_id一样
    new UiSelector().resourceId("id")
    #resourceId
    loc_id = 'new UiSelector().resourceId("com.baidu.yuedu:id/webbooktitle")'
    driver.find_element_by_android_uiautomator(loc_id).click()
3.className
    页面上的class属性一般不唯一，多半用在复数定位时候。此时定位相应下标
    new UiSelector().className("className")
    #className复数定位
    loc_class = 'new UiSelector().className("android.widget.TextView")'
    driver.find_elements_by_android_uiautomator(loc_class)[2].click()
4.description
    也是用contenet-des属性定位
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
6.关系定位
    1).父子定位childSelector
    有时候不能直接定位某个元素，但是它的父元素很好定位，这时候就先定位父元素，通过父元素找儿子
    #父子关系childSelector
    son = 'resourceId("com.baidu.yuedu:id/rl_tabs").childSelector(text("小说"))'
    driver.find_element_by_android_uiautomator(son).click()
     2).兄弟定位fromParent
    有时候父元素不好定位，但是跟他相邻的兄弟元素很好定位，这时候就可以通过兄弟元素，找到同一父级元素下的子元素
    #兄弟关系fromParent
    brother = 'resourceId("com.baidu.yuedu:id/lefttitle").fromParent(text("图书"))'
    driver.find_element_by_android_uiautomator(brother).click()



绝对定位 不推荐 路径太长

推荐 相对 定位 

//*[@text='热门']

如果使用 Xpath 不严谨 可以使用  contains函数 辅助 resource-id

//*[@text='推荐' and contains(@resource-id,'title')]
使用AccessibilityId 控件要有
content-desc 属性有值才可以
accessibilityId ：content-desc

不推荐  ：name  无用  class name 也不推荐 

可以使用 self.driver.page_source 获取资源 
然后使用 idea 工具 XpathView 测试 


def test_page_source(self):
       # 获取当前页资源
       xml = self.driver.page_source
       # todo：添加一个写入文件的功能
       self.log_xml(xml)
   def log_xml(self, page_xlm):
       now = datetime.now()
       with open(now.strftime('H%M%S')+'.xml', 'a') as f:
           f.write(page_xlm)

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

