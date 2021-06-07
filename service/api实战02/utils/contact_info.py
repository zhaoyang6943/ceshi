"""
__author__ == 'zhaoyang'
__time__ = '2021-05-11 20:23'
"""
from faker import Faker


class ContactInfo:

    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        self.faker = Faker('zh-CN')
        name = self.faker.name()
        return name

    def get_phonenum(self):
        self.faker = Faker('zh-CN')
        phonenum = self.faker.phone_number()

        return phonenum

    def get_english_name(self):
        self.faker = Faker()
        name = self.faker.first_name()

        return name


if __name__ == '__main__':
    con = ContactInfo()
    print(con.get_name())
    print(con.get_phonenum())
    print(con.get_english_name())