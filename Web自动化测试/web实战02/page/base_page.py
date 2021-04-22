"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 20:32'
"""
import yaml
from selenium import webdriver


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver 的实例化
    """

    # 没有参数传入，  会取默认None ， 如果有参数传入， 会取传入的参数
    def __init__(self, base_driver=None):
        # _init__ 里面是不允许使用return方法的
        # _init__ 是构造函数
        # 每次实例化的时候都会调用_init__，导致页面启动多次；所以，在调用前，判断是否已经有了driver的实例化
        #
        if base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            # 访问 扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("../datas/data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)

            # 访问通讯录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，在5秒内轮询查找元素是否存在
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def find(self, by, ele=None):
        """
        目的：解决大量的样板代码，driver，find，click
        :param by:
        :param ele:
        :return:
        """
        # 两种传入定位元素的方式，提高代码的兼容性
        # 如果传入的是元组，那就只有一个参数
        if ele == None:
            # 比如传入 (By.ID,"username")
            # * 的作用是， 解元组  self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID,"username")
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)
