import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from base.page_base import BasePage



class PageCreditApplication(BasePage):
    """ 额度申请页面 """
    def __init__(self,driver):
        super().__init__(driver)
        self.role = (By.XPATH, "//em[text()='借款账户']")
        self.application = (By.LINK_TEXT,"申请额度")
        self.money = (By.ID, "amount_account")
        self.detail = (By.NAME, "remark")
        self.code = (By.ID, "verifycode")
        self.btn = (By.CSS_SELECTOR, ".btn-submit.btn-md")
        # 成功
        self.success_result = (By.XPATH, '//*[@id="amount_list"]/tr[1]/td[3]')


    def swithch_role(self):
        """ 切换账户 """
        self.base_click(self.role)

    def click_application(self):
        """ 点击申请额度 """
        self.base_click(self.application)

    def credit_application(self,money,detail,code):
        """ 填写申请额度信息 """
        self.base_input(self.money,money)
        self.base_input(self.detail,detail)
        self.base_input(self.code,code)
        self.base_click(self.btn)


    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        pass

