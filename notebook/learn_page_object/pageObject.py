#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/6 19:58 
@Author : Yong
@File : pageObject.py 
@Software: PyCharm
"""

# Page Object Model（POM）简史
# 主要解决UI 改动 测试案例不能用问题
# 设计思路是 吧页面和测试方法  如果UI 改动 只修改页面部分

# 2013 Martin Flower
# https: // martinfowler.com / bliki / PageObject.html

"""
做法 
❖ 以页⾯为单位独⽴建模 
❖ 隐藏实现细节 
❖ 本质是⾯向接⼜编程 
优点 
❖ 减少重复ﬁnd click样板代码 
❖ 易读性提⾼ 
❖ 页⾯修改不影响测试⽤例
"""

# PageObject模式原则解读
# 以页面为单位 单独封装

"""
⽅法意义 
❖ ⽤公共⽅法代表UI所提供的功能 
❖ ⽅法应该返回其他的PageObject或者返回⽤于断⾔的数据 
❖ 同样的⾏为不同的结果可以建模为不同的⽅法 
❖ 不要在⽅法内加断⾔
字段意义
❖ 不要暴露页⾯内部的元素给外部 
❖ 不需要建模UI内的所有元素
"""

# 登录场景
"""
登陆页⾯提供login ﬁndPassword功能
  ❖ Login类 +  login ﬁndPassword⽅法
登录页⾯内的元素有多少并不关⼼，隐藏内部界⾯控件 
登录成功和失败会分别返回不同的页⾯ 
  ❖ ﬁndPassword 
  ❖ loginSuccess 
  ❖ loginFail 
 通过⽅法返回值判断登录是否符合预期
"""

# 基于POM的⽤例组织结构
"""
❖ page：完成对页⾯的封装 
❖ driver：完成对web、android、ios、接⼜的驱动 
❖ testcase：调⽤各类page完成业务流程并进⾏断⾔ 
❖ data：配置⽂件和数据驱动
❖ utils：其他便捷的功能封装，可选
"""

# 编写⽤例顺序
"""
❖ 根据界⾯封装page类与⽅法，实现可以为空 
❖ 编写⽤例，不断重构明确page⾥⽅法的⼊参和返回值 
❖ 开始实现page内的⽅法 
❖ 调试
❖ 整体类似TDD风格
"""
