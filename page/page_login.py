import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from base.page_base import BasePage


class PageLogin(BasePage):
    """ 登录页面 """
    
    def __init__(self, driver):
        super().__init__(driver)
        """ 登录元素定位信息"""
        self.username = (By.ID, "keywords")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")
        self.result_succsess = (By.CLASS_NAME, "a-link1")
        
        self.result_fail = (By.CSS_SELECTOR,"#err > span")


    def get_url(self):
        """ 访问登录页面 """
        self.driver.get(BASE_URL + "/common/member/login")  



    def login(self,username, password):
        """ 登录操作 """

        # 输入用户名
        self.base_input(self.username, username)
        
        # 输入密码
        self.base_input(self.password, password)

        # 点击登录
        self.base_click(self.login_button)

    
    def get_succsess_result(self):
        """ 获取登录成功结果 """
        return self.fd_element(self.result_succsess).text


    def get_fail_result(self):
        """ 获取登录失败结果 """
        return self.fd_element(self.result_fail).text


# if __name__ == '__main__':
#     p1 = PageLogin(Tools.get_driver())
#     p1.get_url()
#     p1.login("12115116391","123abc")