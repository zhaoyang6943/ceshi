"""
__author__ == 'zhaoyang'
__time__ = '2021-05-27 20:31'
"""

# 作业：企业客户标签，添加、删除、编辑
# 数据驱动
# 数据清理，合理的模式
import pytest

from service.api实战02.api.tag.tag import Tag
from service.api实战02.api.wework_api import WeWork


class TestWeWork:

    def setup(self):
        self.tag = Tag()
        self.tag.get_token()

    def test_search(self):
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize('group_name,tag_name',
                             [['tag_group_052001', 'tag_052002'], ['tag_group_052002', 'tag_052003']],
                             ids=['用例01', 'yongli02'])
    def test_add(self, group_name, tag_name):
        r = self.tag.add(group_name=group_name, tag_name=tag_name)
        assert r.json()['errcode'] == 0

        # todo:复用search方法
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_delete(self):
        r = self.tag.search()

        a = r.json()['tag_group'][0]['group_id']
        print(a, type(a))
        r = self.tag.delete(group_id=a)
        assert r.json()['errcode'] == 0

    def test_edit(self):
        r = self.tag.edit(tag_id="etF-5ACAAApB2D_IAJQSMPUlLtbk_MUg", new_name="hahah")
        assert r.json()['errcode'] == 0
