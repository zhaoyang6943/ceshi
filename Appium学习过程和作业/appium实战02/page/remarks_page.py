"""
__author__ == 'zhaoyang'
__time__ = '2021-05-11 21:31'
"""
from appium.webdriver.common.mobileby import MobileBy

from Appium学习过程和作业.appium实战02.page.base_page import BasePage
from Appium学习过程和作业.appium实战02.page.remove_personnel_page import RemovePersonnelPage


class RemarksPage(BasePage):

    def click_editmember(self):
        # 点击编辑成员
        self.find(MobileBy.XPATH,"//*[@text='编辑成员']").click()

        return RemovePersonnelPage(self.driver)