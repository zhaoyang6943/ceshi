"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:29'
"""

# app相关的操作，关闭，启动，重启
from appium import webdriver  # 导入的appium的webdriver

from Appium学习过程和作业.appium实战02.page.base_page import BasePage
from Appium学习过程和作业.appium实战02.page.main_page import MainPage


class App(BasePage):

    def start(self):

        if self.driver == None:
            print("self.driver = None ！ 现在将初始化driver")

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
            self.logging.info("开始启动app——————————————")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            # 复用driver
            print("复用driver")
            # launch_app 启动的是上面配置的app
            self.driver.launch_app()  # 有driver，就直接启用就好了

            # start_activity 启动页面，可以运行过程中启动其他app或者当前app的其他页面
            # 但是必须要传入两个参数（appPackage，包名；appActivity，页面名）
            # self.driver.start_activity()

        return self

    def restart(self):
        self.logging.info("重启app中——————————————")
        # close_app() 关闭app
        self.driver.close_app()  # 关闭app
        self.driver.launch_app()  # 启动app  test_*的用例中teardown，实际上只用关闭app命令就好

    def stop(self):
        self.logging.info("销毁app的driver中——————————————")
        # quit() 销毁这个driver
        self.driver.quit()  # 退出，就会重新初始化driver

    def goto_main(self):
        # 入口，进去首页
        self.logging.info("进去app主页面——————————————")
        return MainPage(self.driver)
