#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/14 10:00 
@Author : Yong
@File : appium_doc.py 
@Software: PyCharm
"""


# $ appium -g 'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_appium\appium.log' --log-timestamp --local-timezone

# 原生 android  Native App
# H5 web Browser  web 元素解析为安卓原生控件   App
# native+web  Hybrid App

# 使用 WebView
# https://developers.google.com/web/tools/chrome-devtools/remote-debugging/webviews?hl=zh-cn
"""
android studio自带的模拟器 6.0版本，更高版本不支持
genymotion android 模拟器6.0
bluestacks、网易mumu默认不支持的
真机或者模拟器，在root后使用hack手段强行打开webview的调试开关， root + xposed 自己编译android系统，打开webview开关
无论是真机，还是模拟器，浏览器都是可以直接调试的。但是app需要看各个app的内嵌webview的设置情况

用 安卓6.0 以下虚拟机  默认是打开 webView 的 
或者用 genymotion

使用真机需要 使用测试版app 

谷歌 6.2 是稳定版的webview 调试工具 
点击 app 如果有webview  
1.打开代理工具
2.电脑chrome浏览器地址栏输入：chrome://inspect/#devices ，
Remote Target
#LOCALHOST
Android SDK built for x86
#EMULATOR-5554
WebView in com.xueqiu.android (44.0.2403.119)
trace




实盘交易
file:///android_asset/h5/modules_new/xueqiu.com/broker/tradeHome.html?hkus_login=false
inspect pause


会看到你所连接的设备的名称和信息，
下面就是当前设备上可以用于在电脑上调试的页面的一下信息，地址、标题、网页大小

如果没有显示设备信息，则表示没有连接好，可以插拔手机或关闭调试模式重开一下）
原文链接：https://blog.csdn.net/byc233518/article/details/52437498/

先判断 页面资源里面 是否有 WebView 元素

"""

# 查看 安卓虚拟机 谷歌浏览器安装包 和 版本
# 如果 app 没有内嵌浏览器 默认使用 google 微信就不是用自己的驱动
"""
报错没有找到 安卓浏览器的驱动 
selenium.common.exceptions.WebDriverException: 
Message: An unknown server-side error occurred while processing the command.
Original error: No Chromedriver found that can automate Chrome '44.0.2403'. 
See https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md for more details. 
You could also try to enable automated chromedrivers download server feature

谷歌浏览器安装包版本 可以在电脑上看到 
WebView in com.xueqiu.android (44.0.2403.119)
44.0.2403.119
可以使用adb 命令 安卓 6.0 以前叫做browser  以后叫chrome
$ adb shell pm list package | grep browser
package:com.android.browser
$ adb shell pm list package | grep chrome
查看浏览器版本 
Yong@luoluo-PC MINGW64 ~/Desktop
$ adb shell pm dump com.android.browser | grep version
      versionCode=23 targetSdk=23
      versionName=6.0-5525988
Yong@luoluo-PC MINGW64 ~/Desktop
$ adb shell pm list package | grep webview
package:com.android.webview
查看webview 版本
Yong@luoluo-PC MINGW64 ~/Desktop
$ adb shell pm dump com.android.webview | grep version
      versionCode=246011910 targetSdk=23
      versionName=44.0.2403.119

Yong@luoluo-PC MINGW64 ~/Desktop
      



"""

# 下载 谷歌浏览内核 路径
# https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
# 淘宝 cnpm 镜像也有
"""
# 下载 规则  chrome 驱动支持最小的浏览器版本 
# 2.20     43.0.2357.0   
# 2.20 的驱动 支持最小版本的浏览器为 43.0.2357.0

# CAPS 配置 webdriver 路径
固定路径
chromedriverExecutable
文件夹
chromedriverExecutableDir	
配置文件 
chromedriverChromeMappingFile

# 文档 https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
"""


# log 获取 webviews
"""
2020-03-22 22:35:19:891 [HTTP] --> GET /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/contexts
2020-03-22 22:35:19:891 [HTTP] {}
2020-03-22 22:35:19:891 [W3C (5b88bc0d)] Calling AppiumDriver.getContexts() with args: ["5b88bc0d-bd7d-448f-92cf-43d3e12cd07f"]
2020-03-22 22:35:19:892 [AndroidDriver] Getting a list of available webviews
# adb 指令 adb.exe -P 5037 -s emulator-5554 shell cat /proc/net/unix  域套接字  进程间通讯
2020-03-22 22:35:19:892 [ADB] Running 'C:\Users\Yong\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 shell cat /proc/net/unix'
2020-03-22 22:35:19:948 [AndroidDriver] Not checking whether webviews have active pages; use the 'ensureWebviewsHavePages' cap to turn this check on
# 找到webvieb 资源
# adb shell cat /proc/net/unix | grep webview
Yong@luoluo-PC MINGW64 ~/Desktop
$ adb shell cat /proc/net/unix | grep webview
00000000: 00000002 00000000 00010000 0001 01 274533 @webview_devtools_remote_13029

Yong@luoluo-PC MINGW64 ~/Desktop
$ adb shell ps 13029
USER      PID   PPID  VSIZE  RSS   WCHAN            PC  NAME
u0_a61    13029 1692  1858392 273536 SyS_epoll_ b72ce685 S com.xueqiu.android

2020-03-22 22:35:19:949 [AndroidDriver] WEBVIEW_12805 mapped to pid 12805
2020-03-22 22:35:19:949 [AndroidDriver] Getting process name for webview
2020-03-22 22:35:19:949 [ADB] Running 'C:\Users\Yong\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 shell ps'
2020-03-22 22:35:19:995 [AndroidDriver] Parsed pid: '12805' pkg: 'com.xueqiu.android' from
2020-03-22 22:35:19:995 [AndroidDriver]     USER      PID   PPID  VSIZE  RSS   WCHAN            PC  NAME
2020-03-22 22:35:19:995 [AndroidDriver]     u0_a61    12805 1692  1746748 201896          0 7380cd88 R com.xueqiu.android

2020-03-22 22:35:19:995 [AndroidDriver] Returning process name: 'com.xueqiu.android'
2020-03-22 22:35:19:995 [AndroidDriver] Found webviews: ["WEBVIEW_com.xueqiu.android"]
2020-03-22 22:35:19:996 [AndroidDriver] Available contexts: ["NATIVE_APP","WEBVIEW_com.xueqiu.android"]
2020-03-22 22:35:19:996 [W3C (5b88bc0d)] Responding to client with driver.getContexts() result: ["NATIVE_APP","WEBVIEW_com.xueqiu.android"]
2020-03-22 22:35:19:997 [HTTP] <-- GET /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/contexts 200 105 ms - 53
2020-03-22 22:35:19:997 [HTTP]
# 切换到webview
2020-03-22 22:35:19:998 [HTTP] --> POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/context
2020-03-22 22:35:19:998 [HTTP] {"name":"WEBVIEW_com.xueqiu.android"}
2020-03-22 22:35:19:998 [W3C (5b88bc0d)] Calling AppiumDriver.setContext() with args: ["WEBVIEW_com.xueqiu.android","5b88bc0d-bd7d-448f-92cf-43d3e12cd07f"]
2020-03-22 22:35:19:998 [AndroidDriver] Getting a list of available webviews
# unix域套接口
2020-03-22 22:35:19:998 [ADB] Running 'C:\Users\Yong\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 shell cat /proc/net/unix'
2020-03-22 22:35:20:029 [AndroidDriver] Not checking whether webviews have active pages; use the 'ensureWebviewsHavePages' cap to turn this check on
# WEBVIEW 进程号 12805
2020-03-22 22:35:20:029 [AndroidDriver] WEBVIEW_12805 mapped to pid 12805
2020-03-22 22:35:20:029 [AndroidDriver] Getting process name for webview
2020-03-22 22:35:20:029 [ADB] Running 'C:\Users\Yong\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 shell ps'
2020-03-22 22:35:20:075 [AndroidDriver] Parsed pid: '12805' pkg: 'com.xueqiu.android' from
2020-03-22 22:35:20:076 [AndroidDriver]     USER      PID   PPID  VSIZE  RSS   WCHAN            PC  NAME
2020-03-22 22:35:20:076 [AndroidDriver]     u0_a61    12805 1692  1746788 202116          0 b3a58632 R com.xueqiu.android

2020-03-22 22:35:20:076 [AndroidDriver] Returning process name: 'com.xueqiu.android'
2020-03-22 22:35:20:076 [AndroidDriver] Found webviews: ["WEBVIEW_com.xueqiu.android"]
2020-03-22 22:35:20:076 [AndroidDriver] Available contexts: ["NATIVE_APP","WEBVIEW_com.xueqiu.android"]
2020-03-22 22:35:20:076 [AndroidDriver] Connecting to chrome-backed webview context 'WEBVIEW_com.xueqiu.android'
2020-03-22 22:35:20:082 [AndroidDriver] A port was not given, using random free port: 8000
2020-03-22 22:35:20:082 [AndroidDriver] Automated Chromedriver download is disabled. Use 'chromedriver_autodownload' server feature to enable it
2020-03-22 22:35:20:082 [AndroidDriver] Before starting chromedriver, androidPackage is 'com.xueqiu.android'
2020-03-22 22:35:20:082 [Chromedriver] Changed state to 'starting'
# 使用本机  chrome 打开 webview
2020-03-22 22:35:20:085 [Chromedriver] Set chromedriver binary as: C:/Users/Yong/PycharmProjects/HogwartsSDET11/ex_appium/driver/chromedriver2.20.exe
# 强行杀掉 chrome 进程
2020-03-22 22:35:20:085 [Chromedriver] Killing any old chromedrivers, running: wmic process where "commandline like '%chromedriver.exe%--port=8000%'" delete
2020-03-22 22:35:20:229 [Chromedriver] Successfully cleaned up old chromedrivers
2020-03-22 22:35:20:229 [Chromedriver] Cleaning any old adb forwarded port socket connections
# adb 获取tcp 和手机 端口 映射关系
2020-03-22 22:35:20:229 [ADB] List forwarding ports
2020-03-22 22:35:20:229 [ADB] Running 'C:\Users\Yong\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 forward --list'
# 移除所有uiautomator2 映射关系 准备切换到 chromedriver
2020-03-22 22:35:20:255 [ADB] Removing forwarded port socket connection: 12817 
2020-03-22 22:35:20:255 [ADB] Running 'C:\Users\Yong\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 forward --remove tcp\:12817'
# 启动 chromedriver 打印版本  切换到webview 以后和  chromedriver 相互交互 ()
2020-03-22 22:35:20:284 [Chromedriver] Spawning chromedriver with: C:/Users/Yong/PycharmProjects/HogwartsSDET11/ex_appium/driver/chromedriver2.20.exe --url-base=wd/hub --port=8000 --adb-port=5037 --verbose
2020-03-22 22:35:20:317 [Chromedriver] Chromedriver version: '2.20.353145'
2020-03-22 22:35:20:317 [Chromedriver] Chromedriver v. 2.20.353145 does not fully support W3C protocol. Defaulting to MJSONWP
2020-03-22 22:35:20:317 [WD Proxy] Matched '/status' to command name 'getStatus'
2020-03-22 22:35:20:317 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8000/wd/hub/status] with no body
2020-03-22 22:35:20:819 [WD Proxy] Got response with status 200: {"sessionId":"","status":0,"value":{"build":{"version":"alpha"},"os":{"arch":"x86_64","name":"Windows NT","version":"10.0"}}}
2020-03-22 22:35:20:819 [Chromedriver] Starting MJSONWP Chromedriver session with capabilities: {
2020-03-22 22:35:20:819 [Chromedriver]   "desiredCapabilities": {
2020-03-22 22:35:20:819 [Chromedriver]     "chromeOptions": {
2020-03-22 22:35:20:819 [Chromedriver]       "androidPackage": "com.xueqiu.android",
2020-03-22 22:35:20:819 [Chromedriver]       "androidUseRunningApp": true,
2020-03-22 22:35:20:819 [Chromedriver]       "androidDeviceSerial": "emulator-5554"
2020-03-22 22:35:20:819 [Chromedriver]     },
2020-03-22 22:35:20:819 [Chromedriver]     "loggingPrefs": {
2020-03-22 22:35:20:819 [Chromedriver]       "browser": "ALL"
2020-03-22 22:35:20:819 [Chromedriver]     }
2020-03-22 22:35:20:820 [Chromedriver]   }
2020-03-22 22:35:20:820 [Chromedriver] }
2020-03-22 22:35:20:820 [WD Proxy] Matched '/session' to command name 'createSession'
# 再此发起请求以后和 Chromedriver 交互 端口映射 修改为 8000
2020-03-22 22:35:20:820 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8000/wd/hub/session] with body: {"desiredCapabilities":{"chromeOptions":{"androidPackage":"com.xueqiu.android","androidUseRunningApp":true,"androidDeviceSerial":"emulator-5554"},"loggingPrefs":{"browser":"ALL"}}}
2020-03-22 22:35:21:049 [Chromedriver] Webview version: 'Chrome/44.0.2403.119'
2020-03-22 22:35:21:429 [WD Proxy] Got response with status 200: {"sessionId":"e137715c543a70f6d1b92222e9dbc34a","status":0,"value":{"acceptSslCerts":true,"applicationCacheEnabled":false,"browserConnectionEnabled":false,"browserName":"chrome","chrome":{},"cssSelectorsEnabled":true,"databaseEnabled":false,"handlesAlerts":true,"hasTouchScreen":true,"javascriptEnabled":true,"locationContextEnabled":true,"mobileEmulationEnabled":false,"nativeEvents":true,"platform":"ANDROID","rotatable":false,"takesHeapSnapshot":true,"takesScreenshot":true,"version":"44.0.2403.119","webStorageEnabled":true}}
2020-03-22 22:35:21:429 [WD Proxy] Determined the downstream protocol as 'MJSONWP'
2020-03-22 22:35:21:429 [Chromedriver] Changed state to 'online'
2020-03-22 22:35:21:429 [W3C (5b88bc0d)] Responding to client with driver.setContext() result: null
2020-03-22 22:35:21:430 [HTTP] <-- POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/context 200 1432 ms - 14
2020-03-22 22:35:21:430 [HTTP] 
2020-03-22 22:35:21:431 [HTTP] --> GET /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window/handles
2020-03-22 22:35:21:431 [HTTP] {}
2020-03-22 22:35:21:431 [W3C (5b88bc0d)] Driver proxy active, passing request on via HTTP proxy
2020-03-22 22:35:21:431 [WD Proxy] Matched '/wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window/handles' to command name 'getWindowHandles'
2020-03-22 22:35:21:431 [Protocol Converter] Rewrote the original URL '/wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window/handles' to '/wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window_handles' for MJSONWP protocol
2020-03-22 22:35:21:432 [WD Proxy] Proxying [GET /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window_handles] to [GET http://127.0.0.1:8000/wd/hub/session/e137715c543a70f6d1b92222e9dbc34a/window_handles] with body: {}
2020-03-22 22:35:21:458 [WD Proxy] Got response with status 200: {"sessionId":"e137715c543a70f6d1b92222e9dbc34a","status":0,"value":["CDwindow-149654C4-35CD-4F81-8F75-2E38D820D7A0","CDwindow-2DC87FE9-118D-45C7-AAEA-2CFD654577F5","CDwindow-9A190FDB-8CE7-4418-BD52-A530AB97E262"]}
2020-03-22 22:35:21:458 [WD Proxy] Replacing sessionId e137715c543a70f6d1b92222e9dbc34a with 5b88bc0d-bd7d-448f-92cf-43d3e12cd07f
2020-03-22 22:35:21:458 [HTTP] <-- GET /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window/handles 200 27 ms - 206
2020-03-22 22:35:21:458 [HTTP]
# 和chromedriver 交互
2020-03-22 22:35:21:459 [HTTP] --> POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element
2020-03-22 22:35:21:459 [HTTP] {"using":"class name","value":"trade_home_info_3aI"}
2020-03-22 22:35:21:460 [W3C (5b88bc0d)] Driver proxy active, passing request on via HTTP proxy
2020-03-22 22:35:21:460 [WD Proxy] Matched '/wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element' to command name 'findElement'
# 请求发送 后 代理到   http://127.0.0.1:8000
# 后面和selenium
2020-03-22 22:35:21:460 [WD Proxy] Proxying [POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element] to [POST http://127.0.0.1:8000/wd/hub/session/e137715c543a70f6d1b92222e9dbc34a/element] with body: {"using":"class name","value":"trade_home_info_3aI"}
2020-03-22 22:35:21:671 [WD Proxy] Got response with status 200: {"sessionId":"e137715c543a70f6d1b92222e9dbc34a","status":0,"value":{"ELEMENT":"0.4538397614378482-1"}}
2020-03-22 22:35:21:671 [WD Proxy] Replacing sessionId e137715c543a70f6d1b92222e9dbc34a with 5b88bc0d-bd7d-448f-92cf-43d3e12cd07f
2020-03-22 22:35:21:671 [HTTP] <-- POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element 200 212 ms - 156
2020-03-22 22:35:21:671 [HTTP] 
2020-03-22 22:35:21:672 [HTTP] --> POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element/0.4538397614378482-1/click
2020-03-22 22:35:21:672 [HTTP] {"id":"0.4538397614378482-1"}
2020-03-22 22:35:21:673 [W3C (5b88bc0d)] Driver proxy active, passing request on via HTTP proxy
2020-03-22 22:35:21:673 [WD Proxy] Matched '/wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element/0.4538397614378482-1/click' to command name 'click'
2020-03-22 22:35:21:673 [WD Proxy] Proxying [POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element/0.4538397614378482-1/click] to [POST http://127.0.0.1:8000/wd/hub/session/e137715c543a70f6d1b92222e9dbc34a/element/0.4538397614378482-1/click] with body: {"id":"0.4538397614378482-1"}
2020-03-22 22:35:22:359 [WD Proxy] Got response with status 200: {"sessionId":"e137715c543a70f6d1b92222e9dbc34a","status":0,"value":null}
2020-03-22 22:35:22:359 [WD Proxy] Replacing sessionId e137715c543a70f6d1b92222e9dbc34a with 5b88bc0d-bd7d-448f-92cf-43d3e12cd07f
2020-03-22 22:35:22:360 [HTTP] <-- POST /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/element/0.4538397614378482-1/click 200 687 ms - 65
2020-03-22 22:35:22:360 [HTTP] 
2020-03-22 22:35:22:361 [HTTP] --> GET /wd/hub/session/5b88bc0d-bd7d-448f-92cf-43d3e12cd07f/window/handles
2020-03-22 22:35:22:361 [HTTP] {}
2020-03-22 22:35:22:362 [W3C (5b88bc0d)] Driver proxy active, passing request on via HTTP proxy

"""