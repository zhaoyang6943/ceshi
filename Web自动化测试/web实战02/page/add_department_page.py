"""
__author__ == 'zhaoyang'
__time__ = '2021-04-21 21:47'
"""
from Web自动化测试.web实战02.page.base_page import BasePage
from Web自动化测试.web实战02.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):

    def add_department(self):
        """
        点击添加子部门会跳出填写框，输入添加部门信息，点击确定，添加成功后会返回通讯录页面
        :return:
        """
        return ContactPage(self.driver)