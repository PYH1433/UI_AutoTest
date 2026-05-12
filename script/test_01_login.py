import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.page_login import PageLogin
from tools import Tools,GetLog


class TestLogin():

    def setup_method(self):
        driver = Tools.get_driver()
        self.page_login = PageLogin(driver)
        self.page_login.get_url()

    def teardown_method(self):
        Tools.quit_driver()

    def test_login_succsess(self):

        self.page_login.login("12115116391","123abc")

        result = self.page_login.get_succsess_result()
        GetLog.get_log().info(f"登录结果：{result}")

        assert "12115116391" == result


    def test_login_fail(self):

        self.page_login.login("12115116391","123abcd")

        result = self.page_login.get_fail_result()
        GetLog.get_log().info(f"登录结果：{result}")

        assert "密码错误" in result

  



