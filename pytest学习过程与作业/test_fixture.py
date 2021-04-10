# fixture的简单使用
import pytest

# 成功登录的过程，并返回成功登录的结果（假如）
@pytest.fixture()
def login():
    login_result = 'yang，登录成功，欢迎！'
    return login_result


# 一般用例都是在类里面，所以尽量写在类里面。
class TestLoginCase:

    def setup(self):
        print("开始执行================================》")

    def teardown(self):
        print("执行结束================================》")

    def test_login_a(self,login):
        print(f"{login}\n先登录，然后在执行用例a！ok")

    def test_login_b(self):
        print("\n不需要登录，就可以执行的用例b！")

    def test_login_c(self,login):
        print(f"{login}\n需要登录，然后才能执行的用例c！")


if __name__ == '__main__':
    pytest.main(['test_a.py::TestLoginCase','-v'])
