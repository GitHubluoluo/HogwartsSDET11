#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/2 11:35 
@Author : Yong
@File : tset_work.py 
@Software: PyCharm
"""

from ex_pytest.div import div
import pytest
import allure


class TestMyWork:

    # @allure.title("案例标题:DIV测试")
    # @allure.suite('DIV：整数测试')
    @allure.feature('div')
    @allure.story('div_int')
    @pytest.mark.parametrize('param1,param2,expected,msg', [
        (10, 2, 5, '小整数测试'),
        (10000, 5, 2000, '大整数测试'),
        (2000, -2, -1000, '负整数测试'),
        (-2000, 2, -1000, '负整数测试')
    ])
    def test_div_int(self, param1, param2, expected, msg):
        assert div(param1, param2) == expected

    @allure.feature('div')
    @allure.story('div_float')
    @pytest.mark.parametrize('param1,param2,expected,msg', [
        (10, 3, 3.33, '结果浮点数测试'),
        (100.5, 5, 20, '分母浮点数测试'),
        (2000, 5.1, 12, '分子浮点数测试'),
        (5.23, 2.12, 2.2, '全部数测试')
    ])
    def test_div_float(self, param1, param2, expected, msg):
        assert div(param1, param2) == expected

    @allure.feature('div')
    @allure.story('div_str')
    @pytest.mark.parametrize('param1,param2,expected,msg', [
        ('a', 'b', 'c', '字符串测试'),
        (100.5, 'a', 20, '分子字符串测试'),
        ('c', 5.1, 12, '分母字符串测试'),
        (5.23, 2.12, 'n', '结果字符串测试')
    ])
    def test_div_str(self, param1, param2, expected, msg):
        assert div(param1, param2) == expected

    @pytest.mark.exception
    @pytest.mark.parametrize('param1,param2,expected,msg', [
        (100, 0, 0, '分子为0测试'),
        (0, 0, 0, '分母为0测试')
    ])
    def test_div_zero(self, param1, param2, expected, msg):
        assert div(param1, param2) == expected


#  优秀作业 天马
"""
# 进行旧测试数据的清理，测试报告的生成和展示
if __name__ == "__main__":

    # 清空allure_results文件夹，清理掉allure历史记录
    for i in os.listdir(r'allure_results'): os.remove('allure_results/{}'.format(i))
    time.sleep(1)

    # 执行测试并保存allure需要的结果
    os.system('pytest -v --alluredir=allure_results {}'.format(__file__))
    time.sleep(1)

    # 使用allure展示测试报告
    os.system(r'allure serve allure_results')
"""
