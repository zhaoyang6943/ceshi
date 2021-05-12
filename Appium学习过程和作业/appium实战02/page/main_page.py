"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:32'
"""

# 主页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from Appium学习过程和作业.appium实战02.page.base_page import BasePage
from Appium学习过程和作业.appium实战02.page.contactlist_page import ContactlistPage


class MainPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     # driver 后面只是跟类型提示，没有其他作用
    #     self.driver = driver
    """
    基本父类的init方法后，子类就可以删除了
    """

    contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        # click 通讯录

        self.find(*self.contact_element).click()

        return ContactlistPage(self.driver)

