#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/5/28 15:54 
@Author : Yong
@File : app_page_object
@Software: PyCharm
"""
import yaml

"""
Page Object 模式总结
1.使用公共的方法代替页面的功能
2.不要暴露页面的功能和内部细节 定位符和参数
3.不要在方法内部使用断言
4.方法应该返回其他PO
5.不用吧每个页面全都展示出来
6.不同的结果相同的行为应该建模成不同方法 如登录成功和失败

PO 模式封装的主要组成元素
Page对象：完成对页面的封装
Driver对象：完成对web android ios 接口的驱动
测试用例：调用Page对象实现业务并断言
数据封装：配置文件和数据驱动
Utils: 其他功能的封装，改进不足

运行 appium 使用 -g 参数追加 日志 
$ appium -g 'C:\Users\Yong\PycharmProjects\HogwartsSDET11\ex_app_page_object\log\appium.log' --log-timestamp --local-timezone

运行 UI AUTOMATOR VIEWER
> uiautomatorviewer
注： 跑case 的时候不要运行 资源占用冲突


 步搭建流程跑通过 然后在实现里面方法细节

"""



# 日志打印
import logging

logging.basicConfig(level=logging.INFO)
logging.info(logging)


"""
数据驱动
1. 测试数据驱动,测试数据
2. PO定义数据驱动，控件
3. 测试步骤数据驱动 
4. 断言数据驱动



yaml  可以添加 注释  
需要添加 pyyaml
https://pyyaml.org/wiki/PyYAMLDocumentation
"""

list = yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""")
print(list)

# ['Hesperiidae', 'Papilionidae', 'Apatelodidae', 'Epiplemidae']
"""
[...]    # A Python object corresponding to the document.
如果字符串或文件包含多个文档，则可以使用yaml.load_all函数将它们全部加载。
"""
documents = """
---
name: The Set of Gauntlets 'Pauraegen'
description: >
    A set of handgear with sparks that crackle
    across its knuckleguards.
---
name: The Set of Gauntlets 'Paurnen'
description: >
  A set of gauntlets that gives off a foul,
  acrid odour yet remains untarnished.
---
name: The Set of Gauntlets 'Paurnimmen'
description: >
  A set of handgear, freezing with unnatural cold.
"""

for data in yaml.load_all(documents):
    print(data)
"""
{'description': 'A set of handgear with sparks that crackle across its knuckleguards.\n',
'name': "The Set of Gauntlets 'Pauraegen'"}
{'description': 'A set of gauntlets that gives off a foul, acrid odour yet remains untarnished.\n',
'name': "The Set of Gauntlets 'Paurnen'"}
{'description': 'A set of handgear, freezing with unnatural cold.\n',
'name': "The Set of Gauntlets 'Paurnimmen'"}
"""