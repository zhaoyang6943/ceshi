"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 14:57'
"""
import pytest

from Web自动化测试.web实战02.page.main_page import MainPage


class TestAddMember:
    """
    测试用例，在用例这边，我完全不关心页面的元素！
    只关心，和用例的业务场景是不是一致的
    """

    def setup_class(self):
        self.main_page = MainPage()

    def teardown_class(self):
        print("我只执行一次结束！----------------------》")

    def setup(self):
        print("开始计算加法！")

    def teardown(self):
        print("加法计算结束！")

    @pytest.mark.run(order=2)
    # 实现测试数据和页面对象分离
    @pytest.mark.parametrize("username, accid, phone", [["yang1", "0011", "18217276902"]])
    def test_add_member(self, username, accid, phone):
        # main_page = MainPage()
        # 1. 主页面  --》  2. 点击添加成员 --》 3. 添加成员页面 --》4. 获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert phone in name_list

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username, accid, phone", [["yang", "0010", "18217276901"]])
    def test_add_member_fail(self,username, accid, phone):
        data_list = self.main_page.goto_add_member().add_member_fail(username,accid,phone)
        print(type(data_list))
        # data_list 等于 add_member_fail 返回的异常报错数据信息，列表
        # 当列表中不为空的值，是报错的值，取出来打印第一个
        err = [i for i in data_list if i != ""]
        print(err,type(err))
        assert username in err[0]

    def tes1t_xxx(self):
        main_page = MainPage()
        # 1. 主页面  --》  2. 点击添加成员 --》 3. 添加成员的xxx --》 4. 点击添加成员
        # 同一个页面有不同操作的情况，这样就可以自己调用自己的页面功能
        main_page.goto_add_member().add_xxx().add_member()
