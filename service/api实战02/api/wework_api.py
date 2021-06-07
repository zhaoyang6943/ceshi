"""
__author__ == 'zhaoyang'
__time__ = '2021-05-27 20:31'
"""
# 如果有个多个业务线，就可以分多个包；
# wework，下面只放置通用的包

import json

import requests

from service.api实战02.api.base_api import Base


class WeWork(Base):
    # 作用：主要是为了声明类型，python中现在也支持类型了
    token: str = None

    def get_token(self):
        # r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #                  params={"corpid": "wwb2e5afaafb9d6136",
        #                          "corpsecret": "p3tMp8-8U0jMCH4exb-i72ltKMoyN4HwXVb0LsHacoI"
        #                          }
        #
        #                  )

        # 具体的api对象通过这样的设计，可以实现数据化，为以后的自动化生成奠定了一个好的基础
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'method': 'get',
            'params': {
                "corpid": "wwb2e5afaafb9d6136",
                "corpsecret": "p3tMp8-8U0jMCH4exb-i72ltKMoyN4HwXVb0LsHacoI"
            }
        }
        self.logging.info("获取externalcontact的token--------------")
        r = self.request(data)
        self.token = r.json()['access_token']
        assert r.status_code == 200


        # print(r.json())  # json，没有处理，返回没有处理的类似json格式的数据；
        # print(r.json()['access_token'])


    def get_token_user(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'method': 'get',
            'params': {
                "corpid": "wwb2e5afaafb9d6136",
                "corpsecret": "ibVVP3rYxbsOMb1bGCM08pBGOmhlyPxt5xWeeY1TULU"
            }
        }
        self.logging.info("获取user的token--------------")
        r = self.request(data)
        self.user_token = r.json()['access_token']
        assert r.status_code == 200

