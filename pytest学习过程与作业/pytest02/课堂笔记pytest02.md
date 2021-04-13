#### 1. yaml对象转化为python对象

```python
def getdatas():    
    with open("../datas/datas")as f: 
        datas = yaml.safe_load()        
        # safe_load(stram),传入的是文件流，所以将打开的yam文件流传入；        
        # 目的就是将yam对象，转化为python对象
```

注意ymal文件中数据的格式

```yaml
# 整数
int_datas:
  -
    - 1
    - 9
    - 10
  -
    - 10
    - 99
    - 109
  - [100,999,1099]

  - [1000000000000,9999999999999,10999999999999]
####两种方式都行
# int_ids要和int_datas里面的数据数量一致！数据是一个，ids也是一个；数据是多个，ids也是多个；
int_ids:
    - "small_int"
    - "medium_int1"
    - "medium_int2"
    - "large_int"
```

进行调用：

```python
@pytest.mark.parametrize('a,b,c', getdatas()['int_datas'], ids=getdatas()['int_ids'])
def test_add_int(self, a, b, c): 
    '''这个是使用yaml的加法用例'''    
    assert c == self.calc.add(a, b)
```



目的：

今天作业内容：

将装饰器实现的用例参数化，用fixture也实现出来！



#### 2. fixture使用

导包的快捷键：选择后pytest后，Alt+Enter



#### 3. conftest介绍

默认级别：scope=session；可以写成模块级别



#### 4. pytest插件

默认执行用例是：从上到下执行的。

##### 4.1 分布式并发执行测试用例；

pip install pytest-xdist

注意：需要每个用例都要独立，不能有依赖关系，这个是不同进程随机执行用例的。

##### 4.2 单元测试时，用例建议随机执行

pip install pytest-random-order

这样，更能验证出一些问题

##### 4.3 控制用例的执行顺序（举例讲解）

pip install pytest-ordering

由此引出的钩子函数hook！





#### 5. init文件和contest.py区别？

init，导入包时，自动执行使用

contest是自动执行



#### 6. pytest插件

##### 6.1 内置插件（发稿）

hook，在哪呢？pytest内置的hook函数？

site-packages  下  _pytest  下 hookspec.py文件中；

pytest_collection_modifyitems

这个就在里面，功能：先收集所有的用例，通过修改，在放入不同的使用场景中；

##### 6.2 外部插件

通过pip安装的插件

##### 6.3 本地插件

fixture自定义的插件内容，放在contest.py文件中，pytest会自动的发现这些插件



#### 7. 命令执行

pytest的命令行参数    
常用参数：（**ps：windows下用  “双引号”  执行命令！**）    
pytest --collect-only 只收集用例，看到收集的顺序，意味着我知道用例执行的顺序    
pytest -k “add ” 匹配所有名称中包含add的用例（‘add or div’ ‘TestClass’）    
pytest -m mark标签名 -vs   标记,-v详细记录用例执行结果  -s 打印有打印的地方    
pytest --junitxml=./result.xml       生成执行结果文件,后面有用，xml格式，可以后面自己画。    pytest --setup-show 回溯fixture的执行过程（下节课讲解）    
更多的用法使用pytest —help查看帮助文档（建议一一尝试）    
pytest --lf 只运行上次失败的用例    
pytest --ff 先运行上次失败的用例



#### 8. allure 安装

windows安装，

1. 通过maven安装，下载源码解压就ok，bin目录配置环境变量；测试：命令行输入“allure”看是否配置好环境变量；https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.8/

2. python解释器中，添加allure-pytest
3. 自己windows要是jdk1.8环境



#### 9. allure使用

1. pytest --alluredir ./result

   在当前路径下生成测试报告数据

2. allure serve ./result

   在生成测试数据的基础上形成报告



#### 10. python模板配置

![1618319773360](C:\Users\八块腹肌\AppData\Roaming\Typora\typora-user-images\1618319773360.png)



#### 11. 