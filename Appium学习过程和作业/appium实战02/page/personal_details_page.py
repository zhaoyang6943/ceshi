"""
__author__ == 'zhaoyang'
__time__ = '2021-05-11 21:30'
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Appium学习过程和作业.appium实战02.page.base_page import BasePage
from Appium学习过程和作业.appium实战02.page.remarks_page import RemarksPage


class PersonalDetailsPage(BasePage):

    def click_diandiandian(self):
        # 点击三个点
        self.find(MobileBy.XPATH,"//*[@resource-id='android:id/content']/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()
        sleep(3)

        return RemarksPage(self.driver)