#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020/3/8 21:03 
@Author : Yong
@File : tools.py
@Software: PyCharm
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from ex_page_object.page.base_page import BasePage


class Tools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def import_material_img(self, file_path):
        self.get_element(By.CSS_SELECTOR, "a[href='#material/text']").click()
        self.get_element(By.CSS_SELECTOR, "a[href='#material/image']").click()
        self.get_element(By.CLASS_NAME, "js_upload_file_selector").click()
        self.get_element(By.NAME, "uploadImageFile").send_keys(file_path)
        self.wait(10,  expected_conditions.visibility_of_element_located((By.CLASS_NAME, "material_picCard_cnt")))
        self.get_element(By.CLASS_NAME, "js_next").click()
        return self

