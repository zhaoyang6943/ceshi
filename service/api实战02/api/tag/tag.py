"""
__author__ == 'zhaoyang'
__time__ = '2021-05-31 16:42'
"""

import json

import requests

# from service.api实战02.api.wework_api import WeWork
from service.api实战02.api.wework_api import WeWork


class Tag(WeWork):

    def search(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": {}
        }

        return self.request(data)

    def add(self, group_name, tag_name):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "group_name": group_name,
                "tag": [
                    {"name": tag_name}
                ]
            }
        }
        return self.request(data)

    def delete(self, group_id):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {"group_id": group_id}
        }
        return self.request(data)

    def edit(self, tag_id, new_name):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "method": "post",
            "params": {
                "access_token": self.token,
            },
            "json": {
                "id": tag_id,
                "name": new_name
            }
        }
        return self.request(data)
