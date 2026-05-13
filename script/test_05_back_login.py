import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.page_back_login import PageBackLogin
from tools import Tools,GetLog, read_json


class TestBackLogin(object):
    def setup_method(self):
        driver = Tools.get_driver()
        self.back_login = PageBackLogin(driver)
        self.back_login.get_url()

    def teardown_method(self):
        Tools.quit_driver()

    @pytest.mark.parametrize("username,password,img_code,expected",read_json("back_login_data.json"))
    def test_back_login_fail(self,username,password,img_code,expected):

        self.back_login.back_login(username,password,img_code)

        result = self.back_login.get_fail_result()
        GetLog.get_log().info(f"后台登录结果为：{result}")

        assert expected in result

    def test_back_login_succsess(self):

        self.back_login.back_login("admin","HM_2023_test","8888")

        result = self.back_login.get_success_result()
        GetLog.get_log().info(f"后台登录结果为：{result}")

        assert "欢迎光临" in result