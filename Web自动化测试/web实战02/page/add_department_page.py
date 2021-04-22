"""
__author__ == 'zhaoyang'
__time__ = '2021-04-21 21:47'
"""

from time import sleep

from selenium.webdriver.common.by import By

from Web自动化测试.web实战02.page.base_page import BasePage
from Web自动化测试.web实战02.page.contact_page import ContactPage
from selenium.webdriver import ActionChains


class AddDepartmentPage(BasePage):
    # 点击三个点
    a = (By.XPATH, "//*[@class='jstree-anchor jstree-clicked']/span")
    # 点击添加子部门
    b = (By.XPATH, "//*[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']/li[1]/a")
    # 部门名称填写
    c = (By.NAME, "name")
    # 点击确定
    d = (By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]")

    def add_department(self, dep):
        """
        点击添加子部门会跳出填写框，输入添加部门信息，点击确定，添加成功后会返回通讯录页面
        :return:
        """
        # self.find(self.a).click()
        # js = "document.getElementsByClassName('vakata-context jstree-contextmenu jstree-default-contextmenu')[1].style.display='block';"
        # self.driver.execute_script(js)
        self.find(self.b).click()
        sleep(2)
        self.find(self.c).click()
        self.find(self.c).send_keys(dep)
        self.find(self.d).click()

        return ContactPage(self.driver)
