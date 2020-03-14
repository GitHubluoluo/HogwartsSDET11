#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/12 20:17 
@Author : Yong
@File : appium_install.py 
@Software: PyCharm
"""

# 原理
"""
WebDriver script   <->    appium (多种框架)  ->  appliction  
"""

# 安装java 1.8
"""
配置 JAVA_HOME 和环境变量
"""
# 安装node 10
"""
https://nodejs.org/zh-cn/download/releases/
找对应系统的 安装包 安装
"""
# 安装  appium
"""
1.打开VPN
无vpn

用淘宝cnpm （最稳定的方法）
npm install -g cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org 
cnpm install -g appium 


2. npm install -g appium
本地可使用 appium-desktop
https://github.com/appium/appium-desktop/releases

"""
# 安装 Android sdk 可以 安装 android studio
"""
https://developer.android.com/studio#downloads
3.* 版本无tools
可以到
https://www.androiddevtools.cn/ 
下载
配置 ANDROID_HOME sdk目录  和 环境变量  tools 和 platform-tools 环境变量
可以 参考 
https://blog.csdn.net/hahahhahahahha123456/article/details/80651359

https://blog.csdn.net/qq_42391248/article/details/101781994

此时 可以 安装 
npm install -g appium-doctor

然后运行 appium-doctor 测试开发环境

"""


# 安卓模拟器
"""
模拟器使用Android Studio或者sdk中的sdkmanager进行创建
真机需要自备
网易mumu模拟器 https://mumu.163.com/  安卓6.0 可以运行微信
"""


# 最后 安装 appium client

"""
https://github.com/appium/python-client
pip install Appium-Python-Client  
"""

# 创建虚拟机
"""
https://developer.android.google.cn/studio/command-line/avdmanager?hl=zh_cn
命令   avdmanager create avd -n test -k "system-images;android-25;google_apis_playstore;x86"

也可以使用android studio 窗口 创建

运行虚拟机 

使用 adb devices  查看有几台设备可以连接

使用 adb shell 进入虚拟机 内部 

adb 选择不同设备
当有多台设备连接时，需要在命令中夹杂 -s < specific device > 用以区分设备

$ adb devices 
List of devices attached
7330cc21    device
0123456789ABCDEF    device
$ adb -s 7330cc21 shell 


"""
# 使用真机模拟 小米mix2 打开开发者模式
"""
开启
usb 调试
usb 调试授权
usb 安装
关闭
miui 优化
高风险  功能提醒

可以 使用 scrcpy工具  
下载 https://github.com/Genymobile/scrcpy/releases
文档 https://www.zhyong.cn/posts/99d/
投屏 添加环境变量 
运行 scrcpy

"""



# 演练 安装app 找app 入口文件
"""
https://github.com/appium/appium-desktop
演练app：https://sj.qq.com/myapp/detail.htm?apkName=com.xueqiu.android

app信息
打开 git bash 

获取当前界面元元素 顶层窗口
$ adb shell dumpsys activity top | less

获取任务列表：
$ adb shell dumpsys activity activities
安装雪球 
$ adb install -r com.xueqiu.android_12.5_255.apk
Performing Streamed Install
Success

雪球app的入口
com.xueqiu.android/.view.WelcomeActivityAlias

$ adb logcat |grep -i displayed
03-13 12:56:55.235  1649  1670 I ActivityManager: Displayed com.xueqiu.android/.common.splash.SplashActivity: +125ms

Displayed com.xueqiu.android/.common.splash.SplashActivity

或者使用
$ adb shell dumpsys activity activities 
顶层  Display #0 

ACTIVITY MANAGER ACTIVITIES (dumpsys activity activities)
Display #0 (activities from top to bottom):
  Stack #1:
  mFullscreen=true
  isSleeping=false
  mBounds=null
    Task id #14
    mFullscreen=true
    mBounds=null
    mMinWidth=-1
    mMinHeight=-1
    mLastNonFullscreenBounds=null
    * TaskRecord{309cbc2 #14 A=com.xueqiu.android U=0 StackId=1 sz=1}
      userId=0 effectiveUid=u0a80 mCallingUid=u0a80 mUserSetupComplete=true mCallingPackage=com.xueqiu.android
      affinity=com.xueqiu.android
      intent={act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=com.xueqiu.android/.common.splash.SplashActivity}
      origActivity=com.xueqiu.android/.view.WelcomeActivityAlias
      realActivity=com.xueqiu.android/.common.splash.SplashActivity


启动应用
adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S
或者 使用这个 
adb shell am start -W -n com.xueqiu.android/.common.splash.SplashActivity -S


aapt dump badging mobike.apk | grep launchable-activity
apkanalyzer 最新版本的sdk中才有

"""

# Appium Desktop⽤例录制
"""
①打开 appium desktop -> 点击 start inspector session -> 选择 automatic server

advanced Setting 填写app 启动配置项
https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md

{
     “ platformName ”：“ android ”， 使用哪个移动操作系统平台
     “ platformVersion ”：“ 11.0 ”， 移动操作系统版本
     “ deviceName ”：“ iPhone 7 ”，  使用的移动设备或模拟器的种类
     “ automationName ”：“ uiautomator2 ”， 使用哪个自动化引擎
     “ appPackage ” ：“com.xueqiu.android” 您要运行的Android应用的Java软件包
     “ appActivity ”：“.view.WelcomeActivityAlias” app 入口
}

# 测试参数 
{
  "platformName": "android",
  "deviceName": "xiaomi",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "undefined": "uiautomator2"
}

 
"""
# appium python cilant api 地址
"""
https://github.com/appium/appium-desktop 
"""

# 使用 appium servse
"""
运行 appium 使用 -g 参数追加 日志 
$ appium -g 'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log'
[Appium] Welcome to Appium v1.16.0
[Appium] Non-default server args:
[Appium]   logFile: C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log
[Appium] Appium REST http interface listener started on 0.0.0.0:4723

win 10 端口号被占用 
1.在命令窗口中输入命令中输入netstat -ano |findstr "端口号"，然后回车就可以看到这个端口被哪个应用占用。
$ netstat -ano | findstr '4723'
 TCP    0.0.0.0:4723           0.0.0.0:0              LISTENING       10228
2.查看到对应的进程id之后，就可以通过id查找对应的进程名称，使用命令tasklist |findstr "进程id号"
$ tasklist |findstr 10228
node.exe                     10228 Console                    3     54,048 K
3.在命令框中输入如下命令taskkill -f -t -im "进程id或者进程名称"
$ taskkill -f -t -im '10228'
成功: 已终止 PID 10228 (属于 PID 39424 子进程)的进程。



"""