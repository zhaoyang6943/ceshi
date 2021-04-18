"""
__author__ == 'zhaoyang'
__time__ = '2021-04-16 9:37'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestActionChains:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # 鼠标点击操作
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        element_double_click = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        element_right_click = self.driver.find_element(By.XPATH, "//input[@value='right click me']")

        # 定义这些都是鼠标动作
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        # 右击
        action.context_click(element_right_click)

        sleep(3)
        # 执行
        action.perform()
        sleep(3)

    # 鼠标移动操作
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    # 拖拽操作
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.ID, "dragger")
        drop_element = self.driver.find_element(By.XPATH, "//*[@class='item'][1]")

        action = ActionChains(self.driver)
        # 方法一
        # action.drag_and_drop(drag_element, drop_element)

        # 方法二
        # action.click_and_hold(drag_element).release(drop_element)

        # 方法三
        action.click_and_hold(drag_element).move_to_element(drop_element).release()

        action.perform()
        sleep(2)
