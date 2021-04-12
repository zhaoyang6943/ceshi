import pytest

from pytest学习过程与作业.pytest01.Calculator import Calculator
from pytest学习过程与作业.pytest01.test_add import get_add_datas


@pytest.fixture
def login():
    print("登录成功==================》")
    return "hello，我是登录的返回结果，啦啦啦啦啦啦！！！！！！"


# pytest02目录下practicefixture.py文件，使用方法十调用
@pytest.fixture(params=['tom', 'jerry', 'linda'])
def login1():
    print("login1成功！")


# pytest02目录下practicefixture.py文件，使用方法十调用
# 返回参数时，一定要用request，这个是固定的
@pytest.fixture(params=[['tom', 123], ['jerry', 456], ['linda', 789]])
def login2(request):
    print("login2成功！")
    return request.param


# pytest02目录下practicefixture.py文件，使用方法十调用
# 返回参数时，一定要用request，这个是固定的
@pytest.fixture(params=[
    ['tom', 123],
    ['jerry', 456],
    ['linda', 789]
],
    ids=['tom', 'jerry', 'linda']
)
def login3(request):
    print("login3成功！")
    return request.param


# fixture实现计算机的setup和teardown
@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc  # 返回多个值就是元组
    # teardown
    print("teardown")


# fixture实现计算机除法的参数化
@pytest.fixture(params=[[9, 1, 9.0], [99, 33, 3.0], [99999999, 0, "0 cannot be divided"]])
def get_div_datas(request):
    print("fixture实现参数化！")
    print(request.param)
    return request.param


# 在上面的基础上加上了ids
@pytest.fixture(params=[[1, 1, 1], [2, 1, 2]], ids=['aa', 'bb'])
def get_div_datas1(request):
    print(request.param)
    return request.param


# 在上面的基础上从yaml中取值！实现参数化,
@pytest.fixture(params=get_add_datas()['int_datas'], ids=get_add_datas()['int_ids'])
def get_add_datas2(request):
    return request.param
