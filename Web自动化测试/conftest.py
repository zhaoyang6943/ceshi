"""
__author__ == 'zhaoyang'
__time__ = '2021-04-14 16:38'
"""


# from selenium import webdriver
#
#
# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")

def pytest_collection_modifyitems(session, config, items: list):
    # print("这是收集所有测试用例的方法")
    # print(items)
    # items.reverse()  # 这是自己定义的顺序，需要去掉test_的执行顺序的装饰器，才能体现出来！
    # 改写编码集，用例中本来是不支持中文的，通过改写，就可以达到编码改写的目的
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')