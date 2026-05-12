from nt import read
import sys
import os
from unittest import result
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.page_login import PageLogin
from tools import Tools,GetLog,read_json


class TestLogin():

    def setup_method(self):
        driver = Tools.get_driver()
        self.page_login = PageLogin(driver)
        self.page_login.get_url()

    def teardown_method(self):
        Tools.quit_driver()

    @pytest.mark.parametrize("phone, password,expected",read_json("login_data.json"))
    def test_login(self,phone, password,expected):

        self.page_login.login(phone, password)

        if expected == phone:
            result = self.page_login.get_succsess_result()
        else:
            result = self.page_login.get_fail_result()
        GetLog.get_log().info(f"登录结果：{result}")

        assert expected in result

  



