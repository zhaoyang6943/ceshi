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
    # 实现测试数据和页面对象分离
    @pytest.mark.parametrize("username, accid, phone", [["yang", "0010", "18217276901"]])
    def test_add_member(self, username, accid, phone):
        main_page = MainPage()
        # 1. 主页面  --》  2. 点击添加成员 --》 3. 添加成员页面 --》4. 获取成员列表
        name_list = main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert phone in name_list

    def test_xxx(self):
        main_page = MainPage()
        # 1. 主页面  --》  2. 点击添加成员 --》 3. 添加成员的xxx --》 4. 点击添加成员
        # 同一个页面有不同操作的情况，这样就可以自己调用自己的页面功能
        main_page.goto_add_member().add_xxx().add_member()
