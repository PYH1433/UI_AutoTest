import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.page_register import PageRegister
from tools import Tools,GetLog



class TestRegister(object):
    
    def setup_method(self):
        driver = Tools.get_driver()
        self.reg = PageRegister(driver)
        self.reg.get_url()    

    def teardown_method(self):
        Tools.quit_driver()


    def test_register_succsess(self):

        self.reg.register("12115130891","123abc",8888,666666)

        result = self.reg.get_success_result()
        GetLog.get_log().info(f"注册结果为：{result}")

        assert "注册成功" in result


    def test_register_fail(self):

        self.reg.register("12115136391","123abc",8888,666666)

        result = self.reg.get_fail_result()
        GetLog.get_log().info(f"注册结果为：{result}")

        assert "注册抢88现金" == result




