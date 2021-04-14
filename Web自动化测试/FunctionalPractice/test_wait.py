"""
__author__ == 'zhaoyang'
__time__ = '2021-04-14 21:06'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(5)  # 全局设置隐式等待3秒,造成缓冲，比较友好点

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()

        print("okk")
        sleep(3)
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        WebDriverWait(self.driver, 10).until(wait)  # wait和wait()的区别
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        print("123")
