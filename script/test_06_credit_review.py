import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.page_credit_review import PageCreditReview
from page.page_back_login import PageBackLogin
from tools import Tools,GetLog, read_json



class TestCreditReview(object):
    def setup_method(self):
        driver = Tools.get_driver()

        self.back_login = PageBackLogin(driver)
        self.back_login.get_url()
        self.back_login.back_login("admin","HM_2023_test","8888")

        self.credit_rev = PageCreditReview(driver)

        self.credit_rev.menu_click()

        self.credit_rev.search("13640175323")

        self.credit_rev.select_rec()

    def teardown_method(self):
        self.credit_rev.get_shot("credit_review.png")
        Tools.quit_driver()


    def test_credit_review(self):
        self.credit_rev.review("通过","8888")

        self.credit_rev.application_review("13640175323")
        result = self.credit_rev.get_success_result()
        GetLog.get_log().info("额度申请审核结果为：{}".format(result))

        assert "通过" == result




        
