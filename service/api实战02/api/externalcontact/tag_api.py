"""
__author__ == 'zhaoyang'
__time__ = '2021-05-31 16:42'
"""

import json

import jsonpath as jsonpath
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
        self.logging.info("获取externalcontact的tag的search的返回结果----------")
        return self.request(data)

    def add(self, group_name, tag_list):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "group_name": group_name,
                "tag": tag_list
            }
        }
        return self.request(data)

    def add1(self, tag_list, group_name, **kwargs):
        # 可以借鉴 requests.request 与 request.get  .post 的封装思路
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'group_name': group_name,
                'tag': tag_list
            }

        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": json_data
        }
        return self.request(data)

    def delete(self, tag_id_list):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id_list
            }
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

    def clear(self):
        r = self.search()
        tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        # jsonpath，表达式，直接获取到列表
        # jsonpath.jsonpath(r.json(),"$..tag.id")
        r = self.delete(tag_id_list)
        return r
