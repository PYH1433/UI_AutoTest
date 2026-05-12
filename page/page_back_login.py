import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By
from config import BASE_URL
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
        self.success_result = (By.XPATH)
