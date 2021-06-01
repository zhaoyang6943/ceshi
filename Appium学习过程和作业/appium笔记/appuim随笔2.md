# 实战2的PPT

https://pdf.ceshiren.com/ck18/appium2/#/



### appium自动化前置设置

当代码客户端与服务端进行交互的时候，有很多的配置选项，可以视情况进行配置

http://appium.io/docs/en/writing-running-appium/caps/

在自动化测试时，appium会在手机中进行配置一些信息，无论是ios还是android；

尤其在第一次运行的时候，会进行很多的配置，配置一次后，一般第二次就不需要这些配置了，但是appium依旧会进行配置；比如：

**skipDeviceInitialization** ，公共的，跳过设备的初始化，包的安装，运行setting app（也就是appium setting），

他默认是false，不跳过的，每一次都进行初始化，挺影响我们执行速度的，当执行一次后，可以设置成true；当在新设备执行时，一定要是false！！！

无论是ios还是android，在执行自动化的时候，一定会在手机中装上server，UIAutomator2的server；

**appium:skipServerInstallation**，android特有的，跳过服务的安装；

**appium:dontStopAppOnReset**，android特有的，每次执行测试用例的时候，都会给应用先kill掉；如果配置这个参数，就不让它关闭，接着上一次的页面或者执行结果继续执行；



```python
caps["platforName"] = "android"
caps["appPackage"]  = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["deviceName"] = "hogwarts"
caps["noReset"] = "true"
caps["settings[waitForIdleTimeout]"] = 0  # 动态页面，超时等待进行清空
caps["skipDeviceInitialization"] = True  # 跳过服务的安装
```

作用：

能够让server准确的找到本地测试的设备；

还能完成一些动态页面，特殊页面的一些配置；

还能提升我们页面的一些速度；



### 元素定位

测试步骤三要素

- 定位、交互、断言

定位

- id 定位（优先级最高）
- XPath 定位（速度慢，定位灵活）
- Accessibility ID 定位（content-desc）外企，一般都有的这个属性！
- Uiautomator 定位（仅Android 速度快，语法复杂）
- predicate 定位（仅 iOS ）

### XPath定位

类似于数据库中SQL语句，查询数据库信息；

也是遵循了W3C协议；有很多查询xml的方法

https://www.w3.org/TR/xpath-functions/

xpath表达式常用用法：

1、逻辑运算符 （not、and 、or等）

2、表达式 （contains、ends_with、starts_with等）



### XPath 定位方法

绝对定位: 不推荐

相对定位：

//*

//*[contains(@resource-id, ‘login’)]（重点）

//*[@text=‘登录’] （重点）

//*[contains(@resource-id, ‘login’) and contains(@text, ‘登录’)] （重点）

//*[contains(@text, ‘登录’) or contains(@class, ‘EditText’)]（了解）

//*[ends-with(@text,'号') ] | //*[starts-with(@text,'姓名') ] 两个定位的集合列表（了解）

//*[@clickable=“true"]//android.widget.TextView[string-length(@text)>0 and string-length(@text)<20]（了解）

//*[contains(@text, ‘看点')]/ancestor::*//*[contains(@class, ‘EditText’)] （轴）（了解）

//title[@*] 选取所有带有属性的title元素

### po设计

PlantUML Server

一定要写用例，设计它！

### Faker

使用faker设置随机信息，测试用

```python
from faker import Faker
name = "test" + faker.name()
phone = faker.phone_number()
```

### 滑动操作封装使用！

```python
self.driver.swipe(start_x, start_y, end_x, end_y, duration)
```