# Generated by Selenium IDE


from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        pass
        # self.driver.quit()
  
    def test_seleniumtesthome(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        self.driver.find_element(By.CSS_SELECTOR, ".topic-21848 .title >a").click()

