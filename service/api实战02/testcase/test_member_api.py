"""
__author__ == 'zhaoyang'
__time__ = '2021-06-07 15:08'
"""
import allure
import pytest

from service.api实战02.api.contact.member import User
from service.api实战02.utils.contact_info import ContactInfo

ContactInfo = ContactInfo()

@allure.title("用户添加测试用例")
@allure.feature("用例")
class TestUser:
    def setup_class(self):
        self.user = User()
        self.user.get_token_user()


    def teardown_class(self):
        pass

    @allure.title("用户添加正向用例")
    @allure.story("正常添加")
    @pytest.mark.parametrize('name,mobile,userid',
                             [[ContactInfo.get_name(),ContactInfo.get_phonenum(),ContactInfo.get_english_name()],
                              [ContactInfo.get_name(),ContactInfo.get_phonenum(),ContactInfo.get_english_name()]],
                             ids=['数据1','数据2'])
    def test_add(self,name,mobile,userid):
        global a
        r = self.user.add_user(name=name,
                               mobile=mobile,
                               userid=userid
                               )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        a = userid
        print(a)
        # todo:判断是否增加成功
        r = self.user.search(a)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @allure.title("添加异常用例")
    def test_add_error(self,get_error_datas):
        r = self.user.add_user(name=get_error_datas[1],
                               mobile=get_error_datas[2],
                               userid=get_error_datas[0]
                               )
        assert r.status_code == 200
        assert get_error_datas[3] in r.json()['errmsg']