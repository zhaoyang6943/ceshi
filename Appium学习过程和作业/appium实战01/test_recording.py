"""
__author__ == 'zhaoyang'
__time__ = '2021-04-23 22:25'
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["settings[waitForIdleTimeout]"] = 0  # 设置为0后，动态页面查找元素就不会等待10s了
        caps["noReset"] = "true"

        # 最重要的，与服务建立连接。 这就是客户端和服务端建立连接的方式
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源销毁
        self.driver.quit()

    def test_daka(self):
        # 测试用例
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()

        # 动态设置：update_settings()  或者  setup中设置
        # self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']").click()
