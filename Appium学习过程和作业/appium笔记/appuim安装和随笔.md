### app测试的时代背景



我们面临的问题

- 按月发布->按周发布->按小时发布
- 多端发布: Android、iOS、微信小程序、h5
- 多环境发布: 联调环境、测试环境、预发布环境、线上环境
- 多机型发布: 众多设备型号、众多系统版本
- 多版本共存: 用户群体中存在多个不同的版本
- 历史回归测试任务: 成百上千条业务用例如何回归



总结：加班 + 背锅



### Appuim介绍

跨语言Java、Python、nodejs等

跨平台

- Andoid、iOS
- Windows、Mac

底层多引擎可切换

生态丰富，社区强大





### Appuim框架结构

了解结构，方便定位问题



![1619180567002](C:\Users\八块腹肌\AppData\Roaming\Typora\typora-user-images\1619180567002.png)



客户端：按照协议发送给服务端，给服务端，操作手机端

服务端：

手机端



### Appuim为什么可以测试这么多？

大集装箱，下装了很多东西；扩展性很强！



### Appuim工作引擎

有ios'

有android

有web



### Appuim工作环境安装

android：java环境、sdk环境

Appuim：node环境

Android 环境配置

https://ceshiren.com/t/topic/2270

iOS 环境配置

https://ceshiren.com/t/topic/5530

几点建议：

1、Appium Desktop版本不要太老1.15以上，1.19.1可以

2、Java 1.8

3、SDK build-tools/ 下对应的版本，需要使用<=29的版本



环境安装：
https://ceshiren.com/t/topic/11849



### Android自动化前提依赖

Appium Desktop：入门学习工具

设备：模拟器（网易mumu）或真机

Android SDK

其它 Appium 环境



### 与mumu建立连接

打开命令行，打开mumu；

命令行输入：adb connect 127.0.0.1:7555    # 自己电脑与mumu建立连接

adb shell   # 打开mumu的命令行
exit    # 断开mumu的命令行连接

adb devices  # 查看当前电脑上连接的mumu模拟器信息



### windows怎么打开终端？

1. cmd
2. gitbash，下载git的时候



### 定位？



### 打开手机的开发者模式

设置里面-关于手机-点击版本号7下；会处于开发者选项模式。



返回关于手机页面，有个开发者选项按钮，里面有USB调试模式

（ps：模拟器是默认打开的）





### 怎么安装apk？

adb install （把要安装的文件拖进去），点击回车就好



### 怎么打开时，直接就是自己的apk？

**appActivity**

空白页，才能进入的首页；空白页就是启动页

空白页-启动页，加载时间。。。

首页的加载

**appPackage**

java包，唯一的名字



一般想要启动应用的话，一定要拿到，包名和启动页的名字！！但是怎么获取呢？

https://mumu.163.com/help/func/20190129/30131_797867.html

mumu的开发者模式中有命令可以拿到。第六条命令！

cmp=com.tencent.wework/.launch.LaunchSplashActivity

斜杠前面是包名，斜杠后面是空白页



设置时：

“platformName”   “android”

“appPackage”  “com.tencent.wework”

“appActivity”  “.launch.LaunchSplashActivity”

“deviceName”  “hogwarts”

“noReset”  “true”   # 不进行将缓存清空



![1619186482835](C:\Users\八块腹肌\AppData\Roaming\Typora\typora-user-images\1619186482835.png)





解释：为什么是从空白页进去呢？

因为，有些从首页或者其他页面进去的话，有些应用会将这些判断为不合法信息；从启动页是最稳妥的方式。



### 开发者选项里面有个指针位置



作用，可以看坐标



### PPT地址

https://pdf.ceshiren.com/ck18/appium1/#/10



### 抓取手机端日志

adb logcat

adb logcat > log.log  # 将日志文件保存在当前路径下

adb logcat | findstr "appium"



抓取手机端appium的信息日志，查看为什么运行时间这么慢！？

![1619360181606](C:\Users\八块腹肌\AppData\Roaming\Typora\typora-user-images\1619360181606.png)



setting=设置后，时间明显提升非常多！



![1619360343115](C:\Users\八块腹肌\AppData\Roaming\Typora\typora-user-images\1619360343115.png)