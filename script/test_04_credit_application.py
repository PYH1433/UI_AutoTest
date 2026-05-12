import sys
import os
from unittest import result
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.page_login import PageLogin
from page.page_credit_application import PageCreditApplication
from tools import Tools,GetLog,read_json



class TestCreditApplication(object):

    def setup_method(self):
        driver = Tools.get_driver()
        self.credit_app = PageCreditApplication(driver)
        open_login = PageLogin(driver)
        open_login.get_url()
        open_login.login("13640175323","123abc")

    def teardown_method(self):
        Tools.quit_driver()

    @pytest.mark.parametrize("money,detail,code",read_json("credit_data.json"))
    def test_credit_application(self,money,detail,code):
        self.credit_app.swithch_role()
        self.credit_app.click_application()
        self.credit_app.credit_application(money,detail,code)

        result = self.credit_app.get_success_result()
        GetLog.get_log().info(f"额度申请结果：{result}")

        
        assert money == result

        # 截图
        self.credit_app.get_shot("credit_application.png")
