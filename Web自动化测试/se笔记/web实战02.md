## 标题

web 企业微信实战

## 课程价值

- 了解 PageObject 原理及六大原则
- 掌握PageObject 封装思想
- PageObject结合UI自动化测试实战

## 大纲

- PageObject 原理及六大原则
- 企业微信建模
- BasePage的封装
- 添加联系人测试用例

## 时长

120分钟

## 课堂源码链接

> [https://gitlab.stuq.ceshiren.com/ck/ck18/HogwartsSDET18 22](https://gitlab.stuq.ceshiren.com/ck/ck18/HogwartsSDET18)

## 实战内容

### 为什么需要PageObject设计模式

想象一下，一个添加成员用例需要怎么做：

1. 登录_login页面
2. 登录后进入首页_main页面
3. 点击添加成员_main页面
4. 填写添加信息_add_member页面
5. 点击保存_add_member页面
6. 返回通讯录_add_membe页面
7. 加断言做验证_contact页面

传统的web测试用例

```python
def test_add_member(self):
   self.driver.get(“https://work.weixin.qq.com/wework_admin/frame#index")
   element_locator = (By.LINK_TEXT, “添加成员")
    WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
    self.driver.find_element(*element_locator).click()
    self.driver.find_element(By.NAME, 'username').send_keys("abc")
    self.driver.find_element(By.NAME, 'english_name').send_keys("abc")
    self.driver.find_element(By.NAME, "acctid").send_keys("abc")
    self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_zipCode_input input').click()
    self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="853"]').click()
   assert...
```

如果需要多添加一个步骤，从首页->通讯录->添加成员应该怎么改

1. 登录_login页面
2. 进入首页_main页面
3. 点击通讯录_main页面
4. 点击添加成员_contact页面
5. 填写添加信息_add_member页面
6. 点击保存_add_member页面
7. 返回通讯录_add_member页面
8. 加断言做验证_contact页面

对应的自动化测试代码

```python
def test_add_member(self):
   self.driver.get(“https://work.weixin.qq.com/wework_admin/frame#index")
   element_locator = (By.LINK_TEXT, “添加成员")
    WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
    self.driver.find_element(*element_locator).click()
    self.driver.find_element(By.NAME, 'username').send_keys("abc")
    self.driver.find_element(By.NAME, 'english_name').send_keys("abc")
    self.driver.find_element(By.NAME, "acctid").send_keys("abc")
    self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_zipCode_input input').click()
    self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="853"]').click()
   assert...
```

#### 传统UI自动化测试用例的问题

- 无法适应UI变化，UI变化会导致大量的case需要修改
- 无法清晰表达业务用例场景
- 大量的样板代码driver find click

### PageObject原理以及六大原则

#### 参考资料与官网链接

selenium 官方网站：

> [Page object models :: Documentation for Selenium 10](https://www.selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/)

马丁福勒个人博客

> [PageObject 14](https://martinfowler.com/bliki/PageObject.html)

#### PO设计思想



[![image](https://ceshiren.com/uploads/default/optimized/2X/6/6a3a86d8eccd1b840f8c661c298af193f66e75ca_2_400x330.jpeg)image948×783 113 KB](https://ceshiren.com/uploads/default/original/2X/6/6a3a86d8eccd1b840f8c661c298af193f66e75ca.jpeg)



#### PO六大原则

一定要活学活用，不要死搬硬套

[![image](https://ceshiren.com/uploads/default/optimized/2X/e/ef29c9aed7911696a26b245017b4716811cd0319_2_400x161.jpeg)image1613×629 142 KB](https://ceshiren.com/uploads/default/original/2X/e/ef29c9aed7911696a26b245017b4716811cd0319.jpeg)



### 原则解读

- 方法意义
  - 用公共方法代表UI所提供的功能
  - 方法应该返回其他的PageObject或者返回用于断言的数据
  - 同样的行为不同的结果可以建模为不同的方法
  - 不要在方法内加断言
- 字段意义
  - 不要暴露页面内部的元素给外部
  - 不需要建模UI内的所有元素

### 实战练习思路

![image](https://ceshiren.com/uploads/default/original/2X/5/5c1135ead535208a39ba55ee948f4f2dcfa64617.png)

### 实战练习-时序图梳理用例

在线绘制plantuml网站

> [http://plantuml.ceshiren.com/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000 18](http://plantuml.ceshiren.com/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)

添加成员时序图

```
@startuml

participant 企业微信主页面 as main

participant 通讯录页面 as contact

participant 添加成员页面 as add_member

main -> contact: 点击通讯录按钮
main -> add_member: 点击添加成员按钮
add_member -> contact : 1. 填写人员信息 \n 2.点击保存
contact -> contact: 获取成员列表
@enduml
```



[![image](https://ceshiren.com/uploads/default/optimized/2X/7/7c3a554aca37b345a08e39de74223b30514ee429_2_600x432.png)image1684×1216 201 KB](https://ceshiren.com/uploads/default/original/2X/7/7c3a554aca37b345a08e39de74223b30514ee429.png)



1. 每个黄色的区块，代表页面对象即 python 中的 class
2. 每条线 的起始端， 代表页面所提供的方法
3. 每条线的结束段， 代表页面返回的对象/ 返回的断言信息

### 实战练习-构造PO模型

1. 实现设置为空
2. 类 → 页面， 方法-> 页面所提供的操作

### 实战练习-编写测试用例

1. 使用pytest
2. 每个页面对象的方法的return
   1. 其他页面的 实例
   2. 用例所需要的断言

### 优化用例

1. 实现测试数据和页面对象分离
2. 元素抽离出来
3. 解决大量的样板代码driver find click

调用关系类图

```
@startuml
'https://plantuml.com/class-diagram


class BasePage {
string _url
find()
finds()
}

class MainPage {
string  _url
tuple  element
goto_contact_page()
goto_add_member_page()
}

class TestAddMember{

test_add_member()
test_add_member_fail()
}
BasePage <|-- MainPage
BasePage <|-- AddMemberPage
MainPage <..TestAddMember
@enduml
```

## 课后调查表单

[https://jinshuju.net/f/oZGBu8 7](https://jinshuju.net/f/oZGBu8)

## 作业



![img](https://ceshiren.com/user_avatar/ceshiren.com/_ad/40/14359_2.png)  

> 企业微信主页面、 通讯录页面 、添加成员页面 、添加部门页面、导入通讯录页面 时序图。(不作为必须完成的作业，主要是梳理业务逻辑使用) plantuml在线生成工具 http://plantuml.ceshiren.com/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000 [[image\]](https://ceshiren.com/uploads/default/original/2X/a/a2b72cde425fce37481c6f0a98f2ca4ba1c63546.png) 注意：需要体现出来页面对象以及页面对象所对应的方法 使用po思想完…