"""
__author__ == 'zhaoyang'
__time__ = '2021-04-14 21:06'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/categories")
        # self.driver.get("https://www.baidu.com/")

        self.driver.implicitly_wait(5)  # 全局设置隐式等待3秒,造成缓冲，比较友好点

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        print("okk")

        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) > 1

        WebDriverWait(self.driver, 10).until(wait)
        # wait和wait()的区别
        # python传参的时候一定不要写括号，如果写括号，就是调用
        # until是传参的用法
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

    def test_wait01(self):
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        print("okk")

        # selenium自带的条件：元素是否可以被点击
        # expected_conditions.element_to_be_clickable

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))

        # until是传参的用法
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

    def test_baidu(self):
        self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, 'su').click()
        self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院 - 主页')
