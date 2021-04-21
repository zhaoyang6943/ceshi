"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 14:41'
"""
from selenium.webdriver.common.by import By

from Web自动化测试.web实战02.page.base_page import BasePage


class ContactPage(BasePage):

    def get_contact_list(self):
        """
        通讯录页面，可以在自己的通讯录页面中 获取通讯列表，无论是填写后，还是导入后
        :return:
        """
        ele_list = self.driver.find_elements(By.XPATH, "//*[@id='member_list']/tr/td[5]")
        print(ele_list)
        name_list = []
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list

    def get_department_list(self):
        """
        通讯录页面，获取部门信息
        :return:
        """
        name_list = []
        return name_list
