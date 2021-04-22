## 标题

Web 企业微信实战1

## 课程价值

- 了解 selenium IDE
- 掌握使用remote复用已有的浏览器
- 掌握使用cookie登陆

## 大纲

- selenium简介
- selenium IDE
- 使用remote复用已有的浏览器
- 使用cookie登陆

## 时长

90分钟

## PPT

## driver下载地址



![img](https://ceshiren.com/user_avatar/ceshiren.com/seveniruby/40/2_2.png) 

> chromedriver的介绍与相关资料地址，https://ceshiren.com/t/topic/3275；
>
> 方便自动化测试工程师查阅 海外版地址 https://chromedriver.storage.googleapis.com/index.html 淘宝CDN https://npm.taobao.org/mirrors/chromedriver?spm=a2c6h.14029880.0.0.3ba675d7DHrpJf appium的配置 …

## 指定driver路径的方式

```
webdriver.Chrome(executable_path="/Users/jaxon/work/driver/chromedriver/chromedriver")
```

## 配置环境变量的方式

```
self.driver = webdriver.Chrome()
```

- chromedriver的配置问题。
  - 下载浏览器对应的driver版本
  - chromedriver配置环境变量
  - 重启命令行以及pycharm
- 学会找报错信息，以及理解报错信息的含义
- 浏览器不要设置缩放！！

## 浏览器调试

```
chrome --remote-debugging-port=9222
```



![img](https://ceshiren.com/user_avatar/ceshiren.com/pegasus-yang/40/180_2.png)  

复用浏览器：https://ceshiren.com/t/topic/3567

> 将浏览器启动程序配置到环境变量path中 Windows系统：将chrome浏览器启动程序chrome.exe所在文件夹配置到环境变量path中 Linux系统：将chrome浏览器启动程序chrome所在文件夹配置到环境变量path中 Mac系统：将chrome浏览器启动程序Google Chrome所在文件夹配置到环境变量path中 验证配置是否正确：WIndows/Linux系统在命令行执…

## 



## 课后作业：

使用序列化cookie的方式登录企业微信，完成添加成员操作