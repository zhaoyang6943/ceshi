"""
__author__ == 'zhaoyang'
__time__ = '2021-05-27 20:31'
"""
import json

import requests


class WeWork:
    # 作用：主要是为了声明类型，python中现在也支持类型了
    token: str = None

    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": "wwb2e5afaafb9d6136",
                                 "corpsecret": "p3tMp8-8U0jMCH4exb-i72ltKMoyN4HwXVb0LsHacoI"
                                 }

                         )

        self.token = r.json()['access_token']
        assert r.status_code == 200
        # print(r.json())  # json，没有处理，返回没有处理的类似json格式的数据；
        # print(r.json()['access_token'])

    def search(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={
                "access_token": self.token
            }
        )

        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add(self, group_name, tag_name):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name,
                              "tag": [
                                  {"name": tag_name}
                              ]
                          }
                          )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def delete(self, group_id):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={"group_id": group_id}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def edit(self,tag_id,new_name):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            params={
                "access_token":self.token,
            },
            json={
                "id":tag_id,
                "name":new_name
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r



