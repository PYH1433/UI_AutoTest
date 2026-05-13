import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By
from config import BAKE_URL
from base.page_base import BasePage


class PageBackLogin(BasePage):
    """ 后台登录页面 """
    def __init__(self,driver):
        super().__init__(driver)
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.img_code = (By.ID, "valicode")
        self.login_button = (By.CLASS_NAME, "login-button")
        # 成功
        self.success_result = (By.XPATH, "/html/body/div[1]/div[3]/ul/li[2]/a/span")
        # 失败
        self.fail_result = (By.ID, "errorMessage")


    def get_url(self):
        self.driver.get(BAKE_URL + "/common/member/login")


    def back_login(self,username,password,img_code):
        self.base_input(self.username,username)
        self.base_input(self.password,password)
        self.base_input(self.img_code,img_code)
        self.base_click(self.login_button)

    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text
