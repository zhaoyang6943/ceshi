## 标题

python pytest 测试实战（二）

## 课程价值

- 理解 Fixture 高级用法
- 理解 pytest 常用插件
- pytest hook 函数
- 掌握 Allure 生成测试报告

## 大纲

- 作业解析
- Fixture 高级用法
- pytest 常用插件
- pytest hook 函数
- Allure 生成测试报告

## 时长

180 分钟

## 脚本编写

![img](https://ceshiren.com/uploads/default/original/1X/c2911d91c1567acaf78af4212b7669f2f61f67c1.png)[GitLab 19](https://gitlab.stuq.ceshiren.com/ck/ck18/HogwartsSDET18)

![img](https://ceshiren.com/uploads/default/original/1X/10f2d759dce6ea753e1e0b2bf9dc52b57a2f433b.png)

### [Sign in 19](https://gitlab.stuq.ceshiren.com/ck/ck18/HogwartsSDET18)

GitLab Enterprise Edition





## 应用

### 作业解析

情况1：浮点数的处理
情况2：除数为0 的处理

### pytest fixture 作用

pytest fixture 官网：[pytest fixtures: explicit, modular, scalable — pytest documentation 6](https://docs.pytest.org/en/stable/fixture.html#fixture)

- Fixture是在测试函数运行前后，由pytest执行的外壳函数，代码可以定制，满足多变的测试需求，功能包括：
  - 定义传入测试中的数据集
  - 配置测试前系统的初始状态
  - 为批量测试提供数据源等
- Fixture 是pytest 用于将测试前后进行预备，清理工作的代码分离出核心测试逻辑的一种机制

### pytest fixture 使用

方法1（推荐）、直接通过函数名，传递到方法中（如果需要返回值，必须使用这种方式）
方法2、使用 `@pytest.mark.usefixtures('login')` ，测试用例前加上装饰器（没有返回值）

### pytest fixture 用法

- Fixture 是为了测试⽤例的执⾏，初始化⼀些数据和⽅法
  - 1、类似 setUp, tearDown 功能，但⽐ setUp, tearDown 更灵活
  - 2、直接通过函数名字调⽤或使用装饰器@pytest.mark.usefixtures(‘test1’)
  - 3、允许使用多个Fixture
  - 4、使用 autouse 自动应用，如果要返回值，需要传fixture函数名
  - 5、作用域（session>module>class>function）
- - -setup-show 回溯 fixture 的执行过程

#### pytest conftest.py 文件的用法

1、conftest.py文件名是不能换的
2、放在项目下是全局的数据共享的地方（全局的配置和前期工作都可以写在这里）
3、一般来说，conftest.py是用来存放fixture 方法的
4、conftest.py 文件就近生效（如果 在不同的文件夹下都有conftest.py）,离测试文件最近的那个conftest.py 生效)

### pytest 插件

```
pip install pytest-ordering  控制用例的执行顺序
pip install pytest-dependency   控制用例的依赖关系
pip install pytest-xdist    分布式并发执行测试用例
pip install pytest-rerunfailures   失败重跑
pip install pytest-assume              多重较验
pip install pytest-random-order  用例随机执行
pip install  pytest-html                    测试报告 
```

### pytest hook 函数

pytest hook 执行顺序图：[定制pytest插件必备之pytest hook的执行顺序 16](https://ceshiren.com/t/topic/8807)

#### 常用的hook 介绍

- pytest_collection_modifyitems

```
item.name = item.name.encode('utf-8').decode('unicode-escape')
item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
```

- pytest_addoption

#### pytest 插件

- 内置插件：pytest内置的 hook 函数
- 外部插件: 通过pip 安装的插件
- 本地插件: fixture 自定义的插件内容，放在 conftest.py 文件中，pytest 会自动的发现这些插件

### allure 安装

- 安装java 环境
- 安装 allure环境
  allure 下载地址：[Central Repository: io/qameta/allure/allure-commandline/2.13.8 6](https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.8/)
- 安装 allure-pytest库
  `pip install allure-pytest`

#### allure 的用法

- Allure2 解析过程：
  - 1. 安装 allure2
  - 1. Allure help 帮助文档
  - 1. 生成 allure 测试结果 ：pytest —alluredir=./report/
  - 1. 展示报告：allure serve ./report
  - 1. 生成最终版本的报告： allure generate ./report
- 在本地搭建一个网站服务（例如：Django）
  - python manage.py runserver ([http://127.0.0.1:8000/ 4](http://127.0.0.1:8000/))

### 课堂练习

- 将上节课的作业，setup/teardown 改造成fixture的形式
- 改造 pytest 识别用例的规则
- 添加命令行默认参数，运行时自动加上日志，并生成测试报告

## 课后作业

- 上节课的作业，使用fixture 实现setup/teardown 功能
- 使用fixture 实现 参数化的功能
- 使用插件完成测试用例顺序的控制
- 改造测试用例的编码，支持中文编码格式（选做）
- 添加命令行参数，使用hook插件实现（拔高，选做）
- 生成测试 报告截图