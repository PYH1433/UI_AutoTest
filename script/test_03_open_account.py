import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.page_open_account import PageOpenAccount
from page.page_login import PageLogin
from tools import Tools,GetLog
from config import *

class TestOpenAccount(object):

    
    def setup_method(self):
        driver = Tools.get_driver()
        self.open_acc = PageOpenAccount(driver)
        open_login = PageLogin(driver)
        open_login.get_url()
        open_login.login("12985109391","123abc")

    def teardown_method(self):
        Tools.quit_driver()


    def test_open_account_succsess(self):
        self.open_acc.open_account(NAME, CARD)

        result = self.open_acc.get_suceess_result()
        GetLog.get_log().info(f"开户结果：{result}")

        assert "OK" in result
