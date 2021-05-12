"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:45'
"""
from faker import Faker

from Appium学习过程和作业.appium实战02.page.app import App
from Appium学习过程和作业.appium实战02.utils.contact_info import ContactInfo


class TestContact:

    def setup_class(self):
        # self.faker = Faker('zh-CN')
        self.contactinfo = ContactInfo()
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    def teardown(self):
        self.app.restart()

    def test_addcontact(self):
        name = "test" + self.contactinfo.get_name()
        phone = self.contactinfo.get_phonenum()
        self.main.goto_contactlist().click_addmember().addmember_bymenual().edit_member(name,phone).find_toast()

    def test_addcontact1(self):
        name = "test" + self.contactinfo.get_name()
        phone = self.contactinfo.get_phonenum()
        self.main.goto_contactlist().click_addmember().addmember_bymenual().edit_member(name,phone).find_toast()


    def test_deletecontact(self):
        # 删除成员用例
        self.main.goto_contactlist().click_firstpersonnel().click_diandiandian().click_editmember().click_remove_personnel().element_confirm()


    def test_deletecontact1(self):
        # 删除成员用例1
        self.main.goto_contactlist().click_firstpersonnel().click_diandiandian().click_editmember().click_remove_personnel().element_confirm()
