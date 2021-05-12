"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:38'
"""

# 选择添加成员的方式页面
# from Appium学习过程和作业.appium实战02.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from Appium学习过程和作业.appium实战02.page.base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_bymenual(self):
        # clcik 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from Appium学习过程和作业.appium实战02.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        # return True
