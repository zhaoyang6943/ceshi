"""
__author__ == 'zhaoyang'
__time__ = '2021-04-22 7:58'
"""
import pytest

from Web自动化测试.web实战02.page.contact_page import ContactPage



class TestAddDep:

    def setup_class(self):
        self.contact_page = ContactPage()

    @pytest.mark.parametrize("dep",["朝阳部门"])
    def test_add_dep(self,dep):
        res = self.contact_page.goto_add_department().add_department(dep).get_department_list()
        print("123")

        # self.driver.refresh()
        assert "朝阳部门" in res