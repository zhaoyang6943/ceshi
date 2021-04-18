## git

#### git ssh配置

- windows下的配置：
  - 下载git bash
  - ssh-keygen -t rsa -C "github邮箱地址:”
  - cd ssh
  - 把rsa.pub 复制内容到github的settings的ssh里面
  - [git@github.com](mailto:git@github.com):a376230095/aaa.git
- linux下的配置：
  - ssh-keygen -t rsa -C "github邮箱地址:”
  - cd ssh
  - 把rsa.pub 复制内容到github的settings的ssh里面



#### git前置条件的配置

- 配置提交用户的名称
  - git config --global user.name “github用户名”
  - git config --global user.email "github邮箱地址”
- 如果没有git项目
  - git clone [git@github.com](mailto:git@github.com):a376230095/aaa.git
  - 会生成aaa的git项目，并自动同步到远程仓库
- 如果是自己新建一个git项目
  - git init 会在当前的目录生成git项目
  - 在github中新建一个空的项目，一定要是空的，获取这个项目的ssh的链接
  - git remote add origin [git@github.com](mailto:git@github.com):a376230095/aaa.git
  - git push -u origin master 这里就是把git的分支提交到master里面，才算是真正的同步

![image](https://ceshiren.com/uploads/default/original/2X/e/eaa76888d1e9d18d58264df22b7f25f3a6bbc977.png)

#### git工作原理

- 工作区workspace
  - 项目文件所在的文件夹里，统称为工作区。
- 暂存区stage
  - 用来保存要提交到本地版本库的所有文件，相当于一个缓存区。
- 版本库repository
  - —个简单的数据库，包含所有用来维护和管理的项目的修订版本和历史的信息。
  - 分为两部分:
    - 本地仓库local
    - 远程仓库remote
- 不同分区的工作与命令的结合
  - git add会把工作区的文件放到暂存区
  - git commit 会把暂存区的文件放到本地版本库
  - git push 把本地版本库放到远程版本库
  - git pull会把远程仓库放到工作区中
  - git clone/fetch会把远程仓库放到本地仓库
  - git checkout可以把本地仓库的内容放到工作区中



#### 开发测试的流程：

- master作为主分支，一般都是要经过测试通过才拉到master分支上
- 开发的时候先把项目拉到develop分支上，每一个开发对各自负责的功能，再把分支弄到各自的feature分支上
- 代码管理者把开发者开发完的分支弄到develop上，等测试把代码的功能测试完成后，就会弄到release分支上
- 大家一起评估这个release版本是否可以上线，可以就弄到master分支上



#### git clone和git pull的区别

- clone是本地没有repository时，将远程repository整个下载过来。
- pull是本地有repository时，将远程repository里新的commit数据(如有的话)下载过来，并且与本地代码merge。相当于git fetch和git merge



#### git命令解析

- git init 创建一个新的git项目
- git add 添加文件到暂存区
  - git add . 添加当前路径的所有文件
  - git add -A 添加所有目录的文件
- git staus 查看工作区和暂存区等的状态
- git commit -m ‘提交的原因’ 会把暂存区的文件放到本地版本库
- git log 查看历史的提交记录，但如果当前版本比较久，无法查看后面版本的提交记录
- git reflog 查看现在，未来，以前的HEAD信息
- git clone url 克隆仓库，包括.git
  - url格式：用户名@服务器地址:仓库地址
  - git clone [git@github.com](mailto:git@github.com):a376230095/aaa.git
- git pull 相当于git fetch和git merge。其意思是先从远程下载git项目里的文件，然后将文件与本地的分支进行merge。
  - git
- git remote add [remote name] [url] 本地仓库和远程仓库建立联系
  - git remote -v 查看远程分支
  - git remote rm 删除远程分支
  - git remote add origin [git@github.com](mailto:git@github.com):a376230095/aaa.git
- git push 推送本地仓库的内容到远程仓库中
  - 首次push的时候git push -u origin master，下次推动直接git push即可
  - 
- git reset [–soft] [–mixed] [–hard] commit的版本 版本回退
  - –mixed：默认项。修改版本库，修改暂存区，保留工作区。会清空暂存区的修改。
  - –soft：修改版本库，保留暂存区，保留工作区。只需要commit即可恢复版本回退前的状态。
  - –hard：修改版本库，修改暂存区，修改工作区。回退最彻底的一种。
  - 例子：
    - git reset --hard HEAD^ 回到上一个版本
    - git reset --hard HEAD^^^ 回到上上上个版本
    - git reset --hard 13d458 回到指定commit的版本
    - git reset --hard HEAD@{4} 回到指定的第4个版本
- git diff 对比文件或者版本信息
  - git diff a.txt 对比工作区的内容和本地仓库有什么不同
    - 比如当前工作区的a.txt 加了一行tong的代码，就会有个+号
  - git diff “HEAD” “HEAD^” 对比当前版本和上一个版本有什么不同
    - 比如说当前版本比上一个版本多了一个a.txt，就会显示- a.txt
- git checkout 可以把仓库的文件重置到工作区中，也可以切换分支
  - git checkout 1.txt 把仓库的1.txt文件放到工作区
  - git checkout 分支名 切换当前分支到指定的分支名上
  - git checkout -b 分支名 创建指定分支，同时切换当前分支到分支上，好像比较常用
- git branch 分支管理，打印当前的分支
  - git branch -r 打印远程仓库的分支
  - git branch -a 打印全部分支
  - git branch 分支名 创建分支，但分支还是没有切换过去
  - git branch -d 分支名 删除分支，如果分支没有merge提交到其他分支，就不给删除
  - git branch -m oldName newName 修改分支名
  - git merge 分支名 将该分支合并到当前分支上
    - 快速合并分支：master和其他分支或者其他和其他分支，在代码上没有冲突，可以快速合并
    - 非快速合并分支：分支之间的代码有冲突，需要人工判断合并之后有没有问题



#### .gitignore的使用

- 作用：把不需要git管理的文件都放在.gitgnore，确保我们的git都是有用的东西

- 使用.gitignore:

  - 创建.gitignore文件
  - 把不要的文件放入.gitgnore文件夹中(支持通配符)

  ```
  *.iml
  /.iead
  .git
  ```



#### 几种git的场景

- 当删除文件的时候，还没commit的恢复方法
  1. git rm 文件或者git add可以保存这次修改，然后git commit -m 即可同步到仓库了
  2. git checkout – 文件 ，可以把文件恢复
- 当文件删除了，也commit，恢复文件的方法
  1. git log去找到文件还在的那个版本
  2. git reset --hard 前六位的commit代码标识，或者git reset --hard HEAD^ 表示回到上一个版本，^^表示回到上上个版本，以此类推
- 推送远程分支
  1. git checkout -b localbranch 切换创建分支
  2. git branch 查看分支是不是创建并切换好了
  3. git push origin localbranch:localbranch 推送本地分支到远程分支
  4. git push origin :localbranch 删除远程分支
- 当通过git pull 拉取代码，本子自己提交commit代码，然后没有及时git push，不给git push的方法
  1. git pull origin master 再一次拉取代码
  2. git push -u origin master 再推送一下代码
  3. 这样就相当于远程推送了我们最新的提交，工作区也是最新的状态



#### pychram的git学习

- 以下的操作再pycharm的cmd操作
- 注：空文件夹git不会上传的
- 加入.gitgnore可以忽略一些文件上传到github上

1. 在github注册一个账号
2. 在项目的cmd中git init 就会创建一个git项目了
3. git status就可以查看哪些文件没有被add进去
4. git add abc.py 就可以add到本地的git了，但是还没完成加进去
5. git commit -m “add abc.py” 表示完全添加到项目里面去了，而且写了备注是add abc.py
   - unable to auto-detect email address出现这个错误，执行以下的命令
   - git config --global user.email “[376230095@qq.com](mailto:376230095@qq.com)”
   - git config --global user.name “tongtong”
6. git remote add origin [https://github.com/a376230095/appium_python_pytest.git 1](https://github.com/a376230095/appium_python_pytest.git) 表示添加到GitHub里面的appium_python_pytest的repo，通常是.git，这个时候还没有真正同步到远程
7. git push -u origin master 这里就是把git的分支提交到master里面，才算是真正的同步
8. 如果没有登录，pycharm会让你登录GitHub的
9. 当你登录之后，可能还会提示你再输入GitHub的账号密码，再cmd中输入



#### git问题集

1. warning: LF will be replaced by CRLF in test1.txt. The file will have its original line endings in working directory

- 原因：使用了windows来编辑，里面的换行符和git本身使用的linux换行符不一样，会出现一些问题
- 解决：
  - 可以不去解决，通常不建议在windows上修改代码，或者使用pycharm等修改代码
  - git config --global core.autocrlf true，但好像不太行，不管了 这个可以让windows的换行符自动变更为linux的

1. pycharm的github什么都配置好了，为什么

- git remote -v 查看远程仓库名称
  - 如果看到是origin https的，需要取消
- git remote rm origin
- git remote add origin [git@github.com](mailto:git@github.com):你的用户名/你的仓库名.git