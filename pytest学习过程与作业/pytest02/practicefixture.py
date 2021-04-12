import pytest


# 最终建议：fixture官网：https://docs.pytest.org/en/stable/fixture.html#fixture
# 一一敲一下


# @pytest.fixture
# def login():
#     print("登录成功==================》")
#     return "hello，我是登录的返回结果，啦啦啦啦啦啦！！！！！！"


@pytest.fixture
def con_db():
    print("连接数据库成功！===========》")
    username = 'hogwarts'
    password = 123
    return username, password


# 装饰器调用多个装饰器
@pytest.fixture()
def login_and_condb(login, con_db):
    print("登录并连接数据库===========》")
    # return "登录并连接数据库===========》"


# 使用方法一，直接将login传入测试的函数中，不传入则没有进行登录进行搜索
# 区别方法四，方法四拿不到返回结果。
def test_search(a, login):
    print("搜索成功！---------》")
    print(login)


# 使用方法二，将多个fixture传入测试的函数中
def test_add_cart(a, login, con_db):
    print("添加购物车！-------》")


# 使用方法三，装饰器自己去调用装饰器，然后给测试的函数使用调用后的结果
def test_login_and_condb(a, login_and_condb):
    print("登录并连接数据库成功--------》")


# 使用方法四：根据能不能拿到返回数据，区别使用不同的装饰器方法
# 该方法，也能达到类似方法一的效果，但是如果login装饰器有返回结果，该方法是拿不到返回结果的！
@pytest.mark.usefixtures('login')
def test_order(a):
    print("下订单成功--------------》")
    print(login)  # 这个是内存地址
    # 留着报错作为警告，实用usefixtures是拿不到返回值的！


# 使用方法五，多个返回参数怎么取值？连接db后，db装饰器是返回两个值的
def test_login_db(a, con_db):
    print("我要连接db--------------》")
    print(con_db)  # 返回的元组
    username, password = con_db
    print(username, password)


# 使用方法六：类似setup作用,每次测试用例运行时，都会先执行的操作（了解！）
# @pytest.fixture(autouse=True)
# def a():
#     print("每条用例在运行前，都先运行我，我是 a 方法！=====》")


# 模块级别，这个模块在执行用例前，调用；
# 有class级别等。。
# 需要，将a写入调用的用例中，如：def test_login_db(a):
@pytest.fixture(scope="module")
def a():
    print("整个模块在执行用例前，先调用我，只调用一次！=====》")


# 使用方法七：pytest --setup-show practicefixture.py
# 查看py文件中的每一个用例，使用的装饰器都是什么
# Open in --> Terminal，命令窗口执行


# 使用方法八：yield，teardown的效果
# yield 右边， 相当于返回值
# yield下面， 相当于teardown
@pytest.fixture()
def open_box():
    print("打开盒子=================》")
    # return "打开盒子成功！-=-=-=-=-=-=-=-=》"
    yield "打开盒子成功！-=-=-=-=-=-=-=-=》"  # yield 右边， 相当于返回值
    print("关闭盒子！")  # yield下面， 相当于teardown


def test_open_box(open_box):
    print(open_box)  # 返回的值，可以拿到
    print("我要打开盒子！------------》")


# 使用方法九：fixture的公共方法conftest.py，
# 名字是固定的！如果fixture创建太多也是看着很乱的，于是就有了contest.py
# fixture的寻找顺序是先在当前目录寻找，如果没有就会到父节点寻找，并不会在兄弟节点寻找

def test_daka(login):
    print("登录后才能打卡----------》")


# 比较实用的方法十：假如登录有多个账号，怎么用fixture实现参数化呢？
# 调用父节点下的conftest，login1，login2，。。方法！

# 01.简单参数化
def test_login1(login1):
    print("login")


# 02. 返回参数是列表，这个是可以返回参数的！
def test_login2(login2):
    print(login2)


# 03. 在02的基础上添加ids，注意看conftest.py中login3元login2的区别
def test_login3(login3):
    print(login3)


# 使用方法十一：实战，怎么将fixture代替setup和teardown？在昨天的计算机用例中实现？
# yield关键字实现

# 01. fixture实现计算机的setup和teardown的测试；
def test_initcalc_class(initcalc_class):
    print("实现计算机的setup和teardown")
    print(initcalc_class.add(1, 2))
    print(initcalc_class)  # 要记住，这个是可以打印返回值


# 02. fixture实现参数化的测试
class TestDiv:

    def test_div_int(self, initcalc_class, get_div_datas):
        '''这个是参数化，没有使用yaml'''
        assert get_div_datas[2] == initcalc_class.div(get_div_datas[0], get_div_datas[1])

    def test_div_cartesian_product(self, initcalc_class, get_div_datas1):
        try:
            assert get_div_datas1[2] == initcalc_class.div(get_div_datas1[0], get_div_datas1[1])
        except ZeroDivisionError:
            print("0 cannot be divided")

    # 我这个是add测试的参数化
    def test_add_int01(self, initcalc_class, get_add_datas2):
        '''这个是参数化，使用yaml'''
        assert get_add_datas2[2] == initcalc_class.add(get_add_datas2[0], get_add_datas2[1])
