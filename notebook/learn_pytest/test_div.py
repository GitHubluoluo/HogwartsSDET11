#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/2/29 18:17 
@Author : Yong
@File : test_work.py
@Software: PyCharm
"""
from ex_pytest.div import div
import pytest
import allure
"""
1. 通过调用pytestpython -m pytest
在第一个（或N个）失败后停止
要在第一个（N）次失败后停止测试过程：

pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures


2. 指定测试/选择测试
Pytest支持从命令行运行和选择测试的几种方法。

在模块中运行测试

pytest test_mod.py
在目录中运行测试

pytest testing/
通过关键字表达式运行测试


3.按节点ID运行测试

每个收集的测试都分配有一个唯一的nodeid名称，该名称由模块文件名后跟说明符（例如类名，函数名和参数化参数）组成，并用::字符分隔。

要在模块中运行特定的测试，请执行以下操作：

pytest test_mod.py::test_func
在命令行中指定测试方法的另一个示例：

pytest test_mod.py::TestClass::test_method

pytest -k "MyClass and not method"
分组 对测试案例进行分组 标记
4. 通过标记表达式运行测试
将运行用@pytest.mark.slow装饰器装饰的所有测试。
然后，您可以将测试运行限制为仅运行标有的测试slow：
pytest -m slow
pytest -m "happy"

或相反，运行除webtest之外的所有测试：
pytest -v -m "not webtest"
5. 创建JUnitXML格式文件
要创建可被Jenkins或其他持续集成服务器读取的结果文件，请使用以下调用：
pytest --junitxml=path

JUnity 风格xml 报告   
$ pytest --junitxml=test_pytest/div_test.xml test_pytest

$ pip install pytest-html
pytest-html 报告   
$ pytest --html=test_pytest/html.html test_pytest
 
allure2 报告框架 https://docs.qameta.io/allure/

https://docs.qameta.io/allure/#_usage
pip install allure-pytest

要使Allure侦听器能够在测试执行过程中收集结果，只需添加--alluredir选项并提供路径即可存储结果。
https://docs.qameta.io/allure/#_python
例如：
$ pytest --alluredir=tmp/my_allure_results test_pytest

要在测试完成后查看实际报告，您需要使用Allure命令行实用程序从结果生成报告。

$ allure serve tmp/my_allure_results

根据生成的测试报告生成 静态html
$ allure generate tmp/my_alluer_results/ -o tmp/alluer_html

$ cd /tmp/my_allure_result 

$ python -m http.server

allure 装饰器
标题 装饰器:
@allure.title("案例标题:整数测试")
"""


@allure.title("Parameterized test title: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [
    (2, 2, 4),
    (1, 2, 5)
])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected


"""
标记 装饰器 3个
@allure.feature和@allure.story用于根据特定于项目的功能/故事细分来标记测试
要标记某些功能或故事属于史诗，请使用以epic_前缀开头的名称。
您可以使用以下命令行选项来指定不同的测试集，以执行传递以逗号分隔的值的列表的操作：
1.--allure-epics
2.--allure-features
3.--allure-stories
$ pytest tests.py --allure-stories story_1,story_2
$ pytest tests.py --allure-features feature2 --allure-stories story2
"""


@allure.story('epic_1')
def test_with_epic_1():
    pass


@allure.story('story_1')
def test_with_story_1():
    pass


@allure.story('story_2')
def test_with_story_2():
    pass


@allure.feature('feature_2')
@allure.story('story_2')
def test_with_story_2_and_feature_2():
    pass

"""
严重 标记
要按严重性级别标记测试，可以使用@allure.severity装饰器。它以allure.severity_level枚举值作为参数。
通过将--allure-severities命令行选项与逗号分隔的严重性级别结合使用，将仅运行具有相应严重性的测试。
$ pytest tests.py --allure-severities normal,critical
"""


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass
"""
5.1 win10 安装 scoop  https://scoop.sh/

管理员模式打开
确保已安装PowerShell 5（或更高版本，包括PowerShell Core）和.NET Framework 4.5（或更高版本）。然后运行：
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
# or shorter
iwr -useb get.scoop.sh | iex
注意：如果遇到错误，则可能需要使用以下命令更改执行策略（即启用Powershell）
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
安装完成后，输入scoop help验证是否成功


5.2安装 git 
scoop install git

$ scoop install git
Installing '7zip' (19.00) [64bit]
7z1900-x64.msi (1.7 MB) [=====================================================================================] 100%
Checking hash of 7z1900-x64.msi ... ok.
Extracting 7z1900-x64.msi ... done.
Linking ~\scoop\apps\7zip\current => ~\scoop\apps\7zip\19.00
Creating shim for '7z'.
Creating shortcut for 7-Zip (7zFM.exe)
'7zip' (19.00) was installed successfully!
Installing 'git' (2.22.0.windows.1) [64bit]
PortableGit-2.22.0-64-bit.7z.exe (41.1 MB) [==================================================================] 100%
......
......
Creating shortcut for Git Bash (git-bash.exe)
Running post-install script...
'git' (2.22.0.windows.1) was installed successfully!


5.3 Demo : 安装 jdk

5.3.1查看 Scoop 还能直接识别哪些 bucket：coop bucket known 

$ scoop bucket known
main
extras
versions
nightlies
nirsoft
php
nerd-fonts
nonportable
java
games
jetbrains

5.3.2 查找JDK scoop search jdk  

$ scoop search jdk
Results from other known buckets...
(add them using 'scoop bucket add <name>')

'java' bucket:
    bucket/adoptopenjdk-hotspot-jre
    bucket/adoptopenjdk-hotspot
    bucket/adoptopenjdk-lts-hotspot-jre
    bucket/adoptopenjdk-lts-hotspot
    bucket/adoptopenjdk-lts-openj9-jre
    bucket/adoptopenjdk-lts-openj9
    bucket/adoptopenjdk-openj9-jre
    bucket/adoptopenjdk-openj9
    bucket/adoptopenjdk-upstream
    bucket/ojdkbuild-full
    bucket/ojdkbuild
    bucket/ojdkbuild10-full
    bucket/ojdkbuild10
    bucket/ojdkbuild11-full
    bucket/ojdkbuild11
    bucket/ojdkbuild12-full
    bucket/ojdkbuild12                                                                                                       
    bucket/ojdkbuild8-full                                                                                                    
    bucket/ojdkbuild8                                                                                                         
    bucket/ojdkbuild9-full                                                                                                    
    bucket/ojdkbuild9                                                                                                         
    bucket/openjdk                                                                                                            
    bucket/openjdk10
    bucket/openjdk11
    bucket/openjdk12
    bucket/openjdk13
    bucket/openjdk14
    bucket/openjdk7-unofficial
    bucket/openjdk9
    bucket/oraclejdk
    bucket/oraclejdk12


5.3.3scoop bucket add java  添加java源

$ scoop bucket add java
Checking repo... ok
The java bucket was added successfully.

5.3.4 scoop install ojdkbuild8 安装java 1.8 

$ scoop install ojdkbuild8
Installing 'ojdkbuild8' (1.8.0.212-1.b04) [64bit]
java-1.8.0-openjdk-1.8.0.212-1.b04.ojdkbuild.windows.x86_64.zip (103.6 MB) [====================================] 100%
Checking hash of java-1.8.0-openjdk-1.8.0.212-1.b04.ojdkbuild.windows.x86_64.zip ... ok.
Extracting java-1.8.0-openjdk-1.8.0.212-1.b04.ojdkbuild.windows.x86_64.zip ... done.
Linking ~\scoop\apps\ojdkbuild8\current => ~\scoop\apps\ojdkbuild8\1.8.0.212-1.b04
'ojdkbuild8' (1.8.0.212-1.b04) was installed successfully!

$ java -version
openjdk version "1.8.0_212-1-ojdkbuild"
OpenJDK Runtime Environment (build 1.8.0_212-1-ojdkbuild-b04)
OpenJDK 64-Bit Server VM (build 25.212-b04, mixed mod

测试 java -version

5.4 安装allure 
scoop install allure
测试 allure --version
$ allure --version
2.13.2
升级
scoop update allure
5.5 


 
6. 参数化 批量修改执行有错误 数据会继续执行
@pytest.mark.parametrize("num1, num2, exception", {
    (10, 5, 2),
    (10, 2, 5),
    (10000, 1, 10000)
})

"""


@pytest.mark.slow
def test_div_int():
    assert div(6, 3) == 2
    assert div(10, 2) == 5
    assert div(1000000, 1) == 1000000

"""
数据部分可以从外导入 json 文件  使用 json.load('1.json')
@pytest.mark.parametrize("num1, num2, exception", json.load('1.json'))
"""
@pytest.mark.parametrize("num1, num2, exception", {
    (10, 5, 2),
    (10, 2, 5),
    (10000, 1, 10000)
})
def test_div_int_all(num1, num2, exception):
    assert div(num1, num2) == exception


@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.555


def test_div_exception():
    assert div(10, 'a') == 0


def test_div_zero():
    assert div(10, 0) is None

