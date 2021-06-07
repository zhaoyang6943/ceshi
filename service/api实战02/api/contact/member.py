
"""
__author__ == 'zhaoyang'
__time__ = '2021-06-02 21:00'
"""
from service.api实战02.api.wework_api import WeWork


class User(WeWork):

    def add_user(self,userid,name,mobile):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "method": "post",
            "params": {
                "access_token": self.user_token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1, 2],
            }

        }
        self.logging.info("获取data信息----------")
        self.logging.info(data)
        self.logging.info("获取user的add_user的返回结果----------")
        return self.request(data)

    def search(self,userid):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "method": "get",
            "params": {
                "access_token": self.user_token,
                "userid": userid
            }
        }
        self.logging.info("获取data信息----------")
        self.logging.info(data)
        self.logging.info("获取user的search的返回结果----------")
        return self.request(data)