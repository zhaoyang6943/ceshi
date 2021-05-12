"""
__author__ == 'zhaoyang'
__time__ = '2021-05-11 20:23'
"""
from faker import Faker


class ContactInfo:

    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return name

    def get_phonenum(self):
        phonenum = self.faker.phone_number()
        return phonenum


if __name__ == '__main__':
    con = ContactInfo()
    print(con.get_name())