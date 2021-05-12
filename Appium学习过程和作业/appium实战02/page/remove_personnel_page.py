"""
__author__ == 'zhaoyang'
__time__ = '2021-05-11 21:31'
"""
# from Appium学习过程和作业.appium实战02.page.contactlist_page import ContactlistPage
from appium.webdriver.common.mobileby import MobileBy

from Appium学习过程和作业.appium实战02.page.base_page import BasePage


class RemovePersonnelPage(BasePage):

    def click_remove_personnel(self):
        # 点击删除成员按钮
        # 弹出确认框后再点击确定按钮
        self.find(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH,"//*[@text='确定']").click()


        from Appium学习过程和作业.appium实战02.page.contactlist_page import ContactlistPage
        return ContactlistPage(self.driver)