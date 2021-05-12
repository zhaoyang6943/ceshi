"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:41'
"""
# from Appium学习过程和作业.appium实战02.page.add_member_page import AddMemberPage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from Appium学习过程和作业.appium实战02.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phone):
        # input name
        # input phonenum
        # clcik 保存

        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("")
        # 通过（android.widget.EditText）属性也能找到元素
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机')]/../android.widget.RelativeLayout//android.widget.EditText").send_keys(
            phone)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        from Appium学习过程和作业.appium实战02.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
