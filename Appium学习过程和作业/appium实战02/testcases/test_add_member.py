"""
__author__ == 'zhaoyang'
__time__ = '2021-04-28 21:47'
"""
from time import sleep

import pytest
from faker import Faker
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class Test_AddMember:

    def setup_class(self):
        self.faker = Faker('zh-CN')
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        caps["settings[waitForIdleTimeout]"] = 0  # 动态页面，超时等待进行清空
        caps["skipDeviceInitialization"] = True  # 跳过初始化设置，（跳过服务的安装）

        # 当使用setup_class后，这个就可以去掉了
        # caps["dontStopAppOnReset"] = True  # 执行完一个用例后，在执行后的页面上继续操作下一个用例

        # 客户端与服务端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        # 资源销毁
        self.driver.quit()

    def setup(self):
        # 初始化
        self.driver.launch_app()

    def teardown(self):
        # 关闭app
        self.driver.close_app()

    @pytest.mark.parametrize('a',['aa','bb'])
    def test_add_member(self,a):
        # faker
        name = "test" + self.faker.name()
        phone = self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        print("123123")
        self.swipe_find('添加成员').click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("")
        # 通过（android.widget.EditText）属性也能找到元素
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/../android.widget.RelativeLayout//android.widget.EditText").send_keys(
            phone)
        sleep(2)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        #

    def swipe_find(self,text,num = 3):
        # num 默认查找次数

        self.driver.implicitly_wait(1)
        for i in range(0,num):
            if i == num-1:
                raise NoSuchElementException(f"找了{i}次，未找到")

            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                # "滑动一页，继续查找

                # 屏幕尺寸会返回一个宽和高
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                # 'width' , 'height'
                start_x = width / 2
                start_y = height * 0.8

                # 从下往上滑动，x轴是没有变化的
                end_x = start_x
                end_y = height * 0.3

                duration = 2000  # ms
                # 最终完成滑动的操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
