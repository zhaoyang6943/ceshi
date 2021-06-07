"""
__author__ == 'zhaoyang'
__time__ = '2021-05-27 20:31'
"""

# 作业：企业客户标签，添加、删除、编辑
# 数据驱动
# 数据清理，合理的模式
# 作业2，添加成员
import pytest
from jsonpath import jsonpath
import logging

from service.api实战02.api.externalcontact.tag_api import Tag


class TestTag:

    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        self.tag.clear()

    def teardown_class(self):
        pass

    def test_search(self):
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # setup中clear，将所有的数据全部清空了，在搜索用例中，可以深层次的再次断言，tag_group,是否为空,长度为零就是空
        assert len(r.json()['tag_group']) == 0

    @pytest.mark.parametrize('group_name,tag_list',
                             [['tag_group_052001', 'tag_052002'], ['tag_group_052002', 'tag_052003']],
                             ids=['用例01', 'yongli02'])
    def test_add(self, group_name, tag_list):
        """
        参数化添加内容，tag_list1，作为列表传值给增加标签接口。
        :param group_name:
        :param tag_list:
        :return:
        """

        tag_list1 = [{'name': tag_list}]
        r = self.tag.add1(group_name=group_name, tag_list=tag_list1)
        assert r.json()['errcode'] == 0

        # todo:复用search方法，取到group_name，判断新增的group_name数据是否成功
        r = self.tag.search()
        assert r.json()['errcode'] == 0
        assert 'tag_group_052001' in [group['group_name'] for group in r.json()['tag_group']]

        # todo:使用jsonpath语法，获取tag_name_list，判断新增的两个tag_name是否成功
        tag_name_list = jsonpath(r.json(), '$..tag[*].name')
        print(tag_name_list)
        # set 方法，简单判断两个值内容是否相同，但是只有全部参数都执行成功后，最终断言才会成功
        assert set(['tag_052002', 'tag_052003']) == set(tag_name_list)

    def test_order(self):
        # 新增标签后，排序是怎么排序的呢？需要测试验证下!
        # 需要明确需求，排序是后端负责还是前端（js）负责
        tag_list = [
            {'name': 'tag_0602001', 'order': 2},
            {'name': 'tag_0602002', 'order': 1},
            {'name': 'tag_0602003', 'order': 3},
        ]

        r = self.tag.add1(tag_list=tag_list, group_name="tag_group_0602001")
        assert r.json()['errcode'] == 0

        # 添加成功后，查看group_name,有没有显示
        r = self.tag.search()
        assert r.json()['errcode'] == 0
        assert 'tag_group_0602001' in [group['group_name'] for group in r.json()['tag_group']]

        # 添加成功后，查看tag_name，的排序情况
        tag_name_list = jsonpath(r.json(), '$..tag[*].order')
        print(tag_name_list)
        # 前端工程师负责排序，所以不验证排序
        # assert ['tag_0602003','tag_0602002','tag_0602001'] == tag_name_list
        # 直接检查order就好
        assert set([2, 1, 3]) == set(tag_name_list)

    def test_delete(self):
        # 删除数据与添加数据尽量区分开，失败的时候可以更好的直观看到feature失败
        # 准备数据的两个方案 1、添加（不要复用上一步的用例，独立添加，除非添加是个很重的工作）2.setup中添加一批可用数据，就不用在每个用例用数据时，再次添加
        # 建议：第一个方案
        # 删除，先添加一个数据，然后删除，


        # todo：判断新增内容是否在search结果里
        a = self.tag.add1([{'name': 'tag_0602011'}], group_name='tag_group_0602011')
        c = self.tag.search()
        # add后，没有必要在调用search方法验证add结果
        for i in jsonpath(a.json(), '$..tag[*].order'):
            if a.json()['tag_group']['tag'][i]['name'] == 'tag_0602011':
                b = a.json()['tag_group']['tag'][i]['id']

        # todo:因为删除只能根据tag_id删除，所以需要拿到添加数据的tag_id信息
        r = self.tag.delete(tag_id_list=b)
        assert r.json()['errcode'] == 0
        r = self.tag.search()
        # todo:业务逻辑验证，判断删除的内容是否已经消失在search结果里

    def test_flow(self):
        # 冒烟测试
        # 线上巡检测试
        # 全流程的测试  添加、修改、删除、查询
        # 重要的测试数据，三年以上的商店，基本的测试流程；一般都是新增的商店。。
        pass

    def test_edit(self):
        r = self.tag.edit(tag_id="etF-5ACAAApB2D_IAJQSMPUlLtbk_MUg", new_name="hahah")
        assert r.json()['errcode'] == 0
