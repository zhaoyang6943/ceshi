"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:35'
"""

# 通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from Appium学习过程和作业.appium实战02.page.add_member_page import AddMemberPage
from Appium学习过程和作业.appium实战02.page.base_page import BasePage
from Appium学习过程和作业.appium实战02.page.personal_details_page import PersonalDetailsPage


class ContactlistPage(BasePage):

    def click_addmember(self):
        # 点击添加成员，进入到添加成员页面
        print("123")
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def click_firstpersonnel(self):
        # 点击第一个人员，后续进行删除该人员的操作
        # count_element = (MobileBy.XPATH,"//*[contains(@text,'共')]")

        self.find(MobileBy.XPATH,"//*[contains(@text,'test')]").click()

        # count = self.swipe_find('共').text
        # print(count)


        return PersonalDetailsPage(self.driver)

    def element_confirm(self):
        # 是不是有添加成员这个元素
        self.swipe_find("添加成员")
        # return True