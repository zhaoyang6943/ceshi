# 默认级别是session级别，放入公共模块下
import pytest


# test_plug_in.py和test_order.py文件为例子，修改执行顺序的函数！
# 收集用例，pytest自带的，放在conftest中，意味着在执行用例时，先执行这个
# pytest --collect-only：只收集用例，看到收集的顺序，意味着我知道用例执行的顺序
import yaml


def pytest_collection_modifyitems(session, config, items: list):
    # print("这是收集所有测试用例的方法")
    # print(items)
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


def get_error_datas():
    try:
        with open("./datas/data_error.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas
            # safe_load(stram),传入的是文件流，所以将打开的yam文件流传入；
            # 目的就是将yam对象，转化为python对象
    except FileNotFoundError:
        with open("../datas/data_error.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas

@pytest.fixture(params=get_error_datas()['add_error'], ids=get_error_datas()['error'])
def get_error_datas(request):
    return request.param