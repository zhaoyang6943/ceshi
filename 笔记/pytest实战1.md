## pytest实战1

python pytest 测试实战（一）

## 课程价值

- pytest 安装
- PyCharm 配置运行pytest测试
- Git 配置（gitlab）
- 理解 pytest 框架结构
- 掌握参数化

## 大纲

- pytest 介绍与安装
- pytest 常用执行参数
- pytest 框架结构
- pytest 参数化与数据驱动

## 时长

90分钟

## 应用

## 参考链接

pytest : * [http://www.pytest.org/ 7](http://www.pytest.org/)
命名规范: [Python风格规范 — Google 开源项目风格指南 5](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id16)
yaml： [YAML Ain’t Markup Language (YAML™) Version 1.2 9](https://yaml.org/spec/1.2/spec.html)

### pytest 介绍

- 单元测试， 代码测试
  - 后面web, app, 接口 以pytest为基础，后面所有自动化课程 都在用pytest
  - python界面 比较主流的单元测试框架，unittest, nose, pytest
  - 入门难度低， 第三方库丰富性，通用性，与allure生成的报告非常的美观

### pytest 安装

- 安装：
  - pip install pytest
  - Pycharm pytest 配置

## git 配置

- git 是一个代码的管理工具，它可以将你的所有的目录都管理起来，包括文件的变更，实现版本号的管理 。
- Pycharm里面也提供了一个界面化的方式来关联Pycharm中的项目同步到GitHub中。
- git常用命令：[https://ceshiren.com/t/topic/7405 15](https://ceshiren.com/t/topic/7405)



[![image](https://ceshiren.com/uploads/default/optimized/2X/e/eaa76888d1e9d18d58264df22b7f25f3a6bbc977_2_800x272.png)image2020×688 85.5 KB](https://ceshiren.com/uploads/default/original/2X/e/eaa76888d1e9d18d58264df22b7f25f3a6bbc977.png)



## pytest 规则

- 测试用例命名规范
- 文件要在test_开头，或者_test结尾
- 类要以Test开头，方法要以test_开头
- 测试类不可以包含__init__()方法

## pytest 运行

- 三种运行方式：
  - 1、 Pycharm 界面运行
  - 2、右键 文件/ 目录 运行
  - 3、使用命令行方式运行

### pytest 常用的命令行参数

常用参数
pytest --collect-only 只收集用例
pytest -k “add ” 匹配所有名称中包含add的用例（‘add or div’ ‘TestClass’）
pytest -m mark标签名 标记
pytest - - junitxml=./result.xml 生成执行结果文件
pytest --setup-show 回溯fixture的执行过程
更多的用法使用pytest —help查看帮助文档

## pytest 框架结构

- 类似的setup,teardown同样更灵活，
- 模块级(setup_module/teardown_module)模块始末，全局的（**优先最高**）
- 函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
- **类级****(setup_class/teardown_class)**只在类中前后运行一次（在类中）
- 方法级(setup_method/teardown_methond)开始于方法始末（在类中）
- **类里面的（**setup/teardown**）**运行在调用方法的前后

## 参数化与数据驱动

- 什么是参数化？
  - 待测试的输入和输出是一组数据, 可以把测试数据组织起来,用不同的测试数据调用相同的测试方法
- 数据驱动？
  - 数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。

### 参数化的用法

- 参数化装饰函数
- ids参数增加可读性
- 叠加参数化

### mark.parametrize参数化

- 场景：测试数据是传⼊的，测试的预期结果也是传⼊的，⼆个不同的参数⼀⼀对应，输⼊的数据经过调⽤执⾏后结果是否与预期⼀致
- 解决：使⽤mark中的@pytest.mark.parametrize进⾏参数化和数据驱动更灵活
- 应用：
  - 1、在**方法，类**上加上装饰器都可以，
  - 2、另外组合方式可以实现更多测试用例的自动生成

## 参考代码

```
https://gitlab.stuq.ceshiren.com/ck/ck18/HogwartsSDET18
```

## 课后作业

- 1、补全计算器（加法 除法）的测试用例
- 2、使用参数化完成测试用例的自动生成
- 3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
- 注意：
  - 使用等价类，边界值，因果图等设计测试用例
  - 测试用例中添加断言，验证结果
  - 灵活使用 setup(), teardown() , setup_class(), teardown_class()