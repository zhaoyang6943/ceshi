"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:38'
"""

# 选择添加成员的方式页面
# from Appium学习过程和作业.appium实战02.page.edit_member_page import EditMemberPage


class AddMemberPage:


    def addmember_bymenual(self):
        # clcik 手动输入添加
        from Appium学习过程和作业.appium实战02.page.edit_member_page import EditMemberPage
        return EditMemberPage()

    def find_toast(self):
        return True