"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 14:42'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Web自动化测试.web实战02.page.base_page import BasePage
from Web自动化测试.web实战02.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 页面的return 分为两个部分
    # 1. 其他页面的 实例
    # 2. 用例所需要的的断言
    # 注意：  不要写成  ContactPage   一定要加上括号

    # 类变量，设置元组，（ps：类里面，方法外面的变量是不需要加self的）
    # 页面元素不需要让 业务用例了解，所以要加私有，符合六大原则中的  不要暴露页面内部的元素给外部~
    __ele_username = (By.ID, "username")
    __ele_accid = (By.ID, "memberAdd_acctid")
    ele_phone = (By.ID, "memberAdd_phone")
    ele_button_save = (By.XPATH, "//*[@class='member_colRight_operationBar ww_operationBar'][2]/a[2]")

    __address_list = (By.ID,"menu_contacts")

    def add_member(self, username, accid, phone):
        """
        添加成员页面，点击添加成员，跳转到通讯录页面
        :return:
        """
        self.find(self.__ele_username).click()
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_accid).send_keys(accid)
        self.driver.find_element(*self.ele_phone).send_keys(phone)
        self.driver.find_element(*self.ele_button_save).click()
        sleep(3)
        return ContactPage(self.driver)

    def add_member_fail(self, username, accid, phone):
        """
        失败填写
        :param username: 添加页面，填写的元素
        :param accid:
        :param phone:
        :return:
        """
        self.driver.find_element(*self.__ele_username).click()
        self.driver.find_element(*self.__ele_username).send_keys(username)
        self.driver.find_element(*self.__ele_accid).send_keys(accid)
        self.driver.find_element(*self.ele_phone).send_keys(phone)
        self.driver.find_element(*self.ele_button_save).click()

        element = self.driver.find_elements(By.XPATH,"//*[@class='ww_inputWithTips_tips']")

        error_list = []
        for ele in element:
            error_list.append(ele.text)

        self.find(self.__address_list).click()
        return error_list

    def add_xxx(self):
        """
        直接返回self，就是自己调用自己本身的实例
        :return:
        """
        return self
