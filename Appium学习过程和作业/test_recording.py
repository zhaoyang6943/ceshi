"""
__author__ == 'zhaoyang'
__time__ = '2021-04-23 22:25'
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver


class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"

        # 最重要的，与服务建立连接。 这就是客户端和服务端建立连接的方式
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        # 测试用例
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
        el2.click()
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/h8q")
        el4.click()
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/g1n")
        el5.click()
        el5.send_keys("祝朝阳")
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/h86")
        el6.click()
