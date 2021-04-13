# 默认级别是session级别，放入公共模块下
import pytest

# from test_div import get_div_datas_calc
import yaml

try:
    from pytest学习过程与作业.pytest01.Calculator import Calculator
    from pytest学习过程与作业.pytest01.test_add import get_add_datas

except ImportError:
    from pytest01.Calculator import Calculator
    from pytest01.test_add import get_add_datas


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


# # pytest02目录下practicefixture.py文件，使用方法十一调用
# fixture实现计算机的setup和teardown
@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc  # 返回多个值就是元组
    # teardown
    print("teardown")


# pytest02目录下practicefixture.py文件，使用方法十一调用
# fixture实现计算机除法的参数化
@pytest.fixture(params=[[9, 1, 9.0], [99, 33, 3.0], [99999999, 0, "0 cannot be divided"]])
def get_div_datas(request):
    print("fixture实现参数化！")
    print(request.param)
    return request.param


# pytest02目录下practicefixture.py文件，使用方法十一调用
# 在上面的基础上加上了ids
@pytest.fixture(params=[[1, 1, 1], [2, 1, 2]], ids=['aa', 'bb'])
def get_div_datas1(request):
    print(request.param)
    return request.param


# pytest02目录下practicefixture.py文件，使用方法十一调用
# 在上面的基础上从yaml中取值！实现参数化,
@pytest.fixture(params=get_add_datas()['int_datas'], ids=get_add_datas()['int_ids'])
def get_add_datas2(request):
    return request.param


# test_plug_in.py和test_order.py文件为例子，修改执行顺序的函数！
# 收集用例，pytest自带的，放在conftest中，意味着在执行用例时，先执行这个
# pytest --collect-only：只收集用例，看到收集的顺序，意味着我知道用例执行的顺序
def pytest_collection_modifyitems(session, config, items: list):
    # print("这是收集所有测试用例的方法")
    print(items)
    # items.reverse()  # 这是自己定义的顺序，需要去掉test_的执行顺序的装饰器，才能体现出来！
    # 改写编码集，用例中本来是不支持中文的，通过改写，就可以达到编码改写的目的
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 下面将test_plug_in.py文件下的两个测试用例添加标签，通过-m参数执行时，就可以执行到他们两个用例
        # pytest test_plug_in.py -m "foo"  # 注意在windows命令下一定要是双引号！
        if 'foo' in item.name:
            item.add_marker(pytest.mark.foo)
        elif 'bar' in item.name:
            item.add_marker(pytest.mark.bar)


# 作业，相加浮点数取值数据
@pytest.fixture(params=get_add_datas()['float_datas'], ids=get_add_datas()['float_ids'])
def get_add_datas_float(request):
    return request.param


# 作业，相加负数取值数据
@pytest.fixture(params=get_add_datas()['negative_datas'], ids=get_add_datas()['negative_ids'])
def get_add_datas_negative(request):
    return request.param

# 给除法提供函数调用取值的功能
def get_div_datas_calc():
    try:
        with open("./datas/calc.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas
            # safe_load(stram),传入的是文件流，所以将打开的yam文件流传入；
            # 目的就是将yam对象，转化为python对象
    except FileNotFoundError:
        with open("../datas/calc.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas


# 作业，相除，整数取值数据
@pytest.fixture(params=get_div_datas_calc()['int_datas'], ids=get_div_datas_calc()['int_ids'])
def get_div_datas_int(request):
    return request.param


# 作业，相除，浮点数取值数据
@pytest.fixture(params=get_div_datas_calc()['float_datas'], ids=get_div_datas_calc()['float_ids'])
def get_div_datas_float(request):
    return request.param

# 作业，相除，负数取值数据
@pytest.fixture(params=get_div_datas_calc()['negative_datas'], ids=get_div_datas_calc()['negative_ids'])
def get_div_datas_negative(request):
    return request.param

# 作业，相除，除数为零取值数据
@pytest.fixture(params=get_div_datas_calc()['zero'], ids=get_div_datas_calc()['zero_ids'])
def get_div_datas_zero(request):
    return request.param