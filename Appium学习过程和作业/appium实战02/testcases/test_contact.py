"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:45'
"""
from Appium学习过程和作业.appium实战02.page.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        self.main.goto_contactlist().click_addmember().addmember_bymenual().edit_member().find_toast()
