"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 14:42'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Web自动化测试.web实战02.page.base_page import BasePage
from Web自动化测试.web实战02.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 页面的return 分为两个部分
    # 1. 其他页面的 实例
    # 2. 用例所需要的的断言
    # 注意：  不要写成  ContactPage   一定要加上括号
    def add_member(self, username, accid, phone):
        """
        添加成员页面，点击添加成员，跳转到通讯录页面
        :return:
        """
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.XPATH, "//*[@class='member_colRight_operationBar ww_operationBar'][2]/a[2]").click()
        sleep(3)

        return ContactPage(self.driver)

    def add_xxx(self):
        """
        直接返回self，就是自己调用自己本身的实例
        :return:
        """
        return self
