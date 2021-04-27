"""
__author__ == 'zhaoyang'
__time__ = '2021-04-27 21:16'
"""
# from appium.webdriver import webdriver
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestHomeWork:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        caps["settings[waitForIdleTimeout]"] = 0  # 动态页面，超时等待进行清空
        caps["skipDeviceInitialization"] = True  # 跳过初始化设置，（跳过服务的安装）

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        sleep(3)