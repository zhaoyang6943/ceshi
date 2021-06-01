"""
__author__ == 'zhaoyang'
__time__ = '2021-05-31 16:45'
"""
import json

import requests


class Base:

    def request(self, request: dict):
        # 为了多协议支持，或者将来协议变更，或者将来方便切换不同的http库，比如requests切换到其他的lib
        if "url" in request:
            return self.http_request(request)
        if "rpc" == request.get("protocol"):
            return self.rpc_request(request)

    def http_request(self,request):
        # 数据解包
        r = requests.request(**request)
        # todo：print这边换成logging！！！打印日志！
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self):
        ...

    def tcp_request(self):
        ...
