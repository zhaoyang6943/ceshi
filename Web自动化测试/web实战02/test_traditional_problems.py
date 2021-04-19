"""
__author__ == 'zhaoyang'
__time__ = '2021-04-19 10:09'
"""

# 传统的自动化用例，有着什么样的问题？
# 1. 代码是没有办法适应ui的变化的,如果10条用例,那么就要修改10个地方;添加必填性信息的时候,也会修改10个地方
# 2. 代码可读性差,没有办法清晰的表达自己的业务逻辑
# 3. 大量的样板代码 driver find click

# 重复就是最严重的的问题，充满着坏味道

# 23种设计模式，page objec
# 马丁福勒个人博客，他提出了这个设计思想
# https://martinfowler.com/bliki/PageObject.html

# selenium的官方文档，都有po设计模式

# 通过po设计思想，和六大原则，介绍
# html的操作层，和具体应用层，分层思想；由此引发的六大原则：