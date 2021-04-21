"""
__author__ == 'zhaoyang'
__time__ = '2021-04-21 22:06'
"""
from Web自动化测试.web实战02.page.base_page import BasePage
from Web自动化测试.web实战02.page.contact_page import ContactPage


class ImportAddressBookPage(BasePage):

    def do_import_address_book(self):
        """
        导入成功后，返回通讯录页面
        :return:
        """
        return ContactPage(self.driver)