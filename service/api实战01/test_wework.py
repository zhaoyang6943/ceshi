"""
__author__ == 'zhaoyang'
__time__ = '2021-05-20 20:37'

这是最传统的代码，下面条一样！
"""
import json

import requests


class TestWeWork:

    def setup(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": "wwb2e5afaafb9d6136",
                                 "corpsecret": "p3tMp8-8U0jMCH4exb-i72ltKMoyN4HwXVb0LsHacoI"
                                 }

                         )

        self.token = r.json()['access_token']
        assert r.status_code == 200

    def test_token(self):
        # token测试
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": "wwb2e5afaafb9d6136",
                                 "corpsecret": "p3tMp8-8U0jMCH4exb-i72ltKMoyN4HwXVb0LsHacoI"
                                 }

                         )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))  # 返回的类似json格式的数据，进行处理后，成为真正的json，并优化显示格式
        print(r.json())  # json，没有处理，返回没有处理的类似json格式的数据；
        print(r.json()['access_token'])
        assert r.status_code == 200

    def test_search(self):
        # 搜索测试
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            }
        )

        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag(self):
        # 添加测试
        # todo:数据唯一性，1. 提前清理数据；2. 使用时间戳代表唯一性
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "group_name": "tag_group_00001",
                              "externalcontact": [
                                  {"name": "tag0001"}
                              ]
                          }
                          )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()['errcode'] == 0

        # todo:代码重复，当标签增加后，需要搜索，再次检查是否添加成功
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            }
        )

        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_tag_delete(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={"group_id": "etF-5ACAAAOJT6Ws1TQh3IfbESCan9QQ"}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
