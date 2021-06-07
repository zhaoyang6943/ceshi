"""
__author__ == 'zhaoyang'
__time__ = '2021-05-31 16:45'
"""
import json

import requests

import logging

from faker import Faker

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("../logs/info.log", encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

class Base:

    def __init__(self):
        self.logging = logger

    def request(self, data: dict):
        # 为了多协议支持，或者将来协议变更，或者将来方便切换不同的http库，比如requests切换到其他的lib
        if "url" in data:
            return self.http_request(data)
        if "rpc" == data.get("protocol"):
            return self.rpc_request(data)

    def http_request(self, data):
        # 数据解包
        r = requests.request(**data)
        # todo：print这边换成logging！！！打印日志！
        self.logging.info("开始打印用例返回结果-----------------")
        self.logging.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self):
        ...

    def tcp_request(self):
        ...

