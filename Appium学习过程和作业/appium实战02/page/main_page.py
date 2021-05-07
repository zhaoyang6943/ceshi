"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:32'
"""

# 主页面
from Appium学习过程和作业.appium实战02.page.contactlist_page import ContactlistPage


class MainPage:

    def goto_contactlist(self):
        # click 通讯录
        return ContactlistPage()

