"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 14:41'
"""
from time import sleep

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By

# from Web自动化测试.web实战02.page.add_department_page import AddDepartmentPage
from selenium.webdriver.support.wait import WebDriverWait

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
        # self.driver.refresh()
        sleep(1)
        ele_list = self.driver.find_elements(By.XPATH,"//*[@class='jstree-container-ul jstree-children jstree-striped jstree-wholerow-ul jstree-no-dots']//a")
        print(ele_list)
        name_list = []
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list

    def goto_add_department(self):
        # 防止循环调用！导入方法里
        from Web自动化测试.web实战02.page.add_department_page import AddDepartmentPage
        # 点击通讯录
        con = (By.XPATH, "//*[@id='menu_contacts']/span")
        # 点击三个点
        a = (By.XPATH, "//*[@class='jstree-anchor jstree-clicked']/span")

        self.find(con).click()
        self.find(a).click()
        return AddDepartmentPage(self.driver)