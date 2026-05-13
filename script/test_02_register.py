import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from page.page_register import PageRegister
from tools import Tools,GetLog, read_json



class TestRegister(object):
    
    @pytest.mark.parametrize("phone,pwd,im_code,ph_code,expected",read_json("register_data.json"))
    def test_register_succsess(self,pg_register,phone,pwd,im_code,ph_code,expected):

        pg_register.register(phone,pwd,im_code,ph_code)

        

        result = pg_register.get_success_result()
        GetLog.get_log().info(f"注册结果为：{result}")

        assert expected in result


    def test_register_fail(self,pg_register):

        self.reg.register("12115836391","123abc",8888,666666)

        result = pg_register.get_fail_result()
        GetLog.get_log().info(f"注册结果为：{result}")

        assert "注册抢88现金" == result




