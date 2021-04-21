"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 14:40'
"""


# 符合第一条原则：用公共的方法代表UI所提供的功能
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Web自动化测试.web实战02.page.add_member_page import AddMemberPage
from Web自动化测试.web实战02.page.base_page import BasePage
from Web自动化测试.web实战02.page.import_address_book_page import ImportAddressBookPage


class MainPage(BasePage):

    def goto_contact(self):
        """
        跳转到通讯录页面，这个和下面的goto_add_member 当做一个就好
        :return:
        """
        ...

    def goto_add_member(self):
        """
        点击通讯录，跳转到添加成员页面
        :return:
        """

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='ww_operationBar']/a[1]")))
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@class='ww_operationBar']/a[1]").click()
        # 返回要跳转页面的实例对象
        return AddMemberPage(self.driver)

    def goto_import_address_book(self):
        """
        跳转导入通讯录页面
        :return:
        """
        return ImportAddressBookPage(self.driver)
