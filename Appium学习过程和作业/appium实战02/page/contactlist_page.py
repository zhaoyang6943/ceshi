"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:35'
"""

# 通讯录页面
from Appium学习过程和作业.appium实战02.page.add_member_page import AddMemberPage


class ContactlistPage:

    def click_addmember(self):
        # 点击添加成员，进入到添加成员页面
        return AddMemberPage()
