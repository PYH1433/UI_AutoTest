import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import Tools

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from base.page_base import BasePage

class PageOpenAccount(BasePage):
    """ 开户页面 """

    def __init__(self,driver):
        super().__init__(driver)
        self.im_open = (By.LINK_TEXT, "立即开通")
        self.name = (By.NAME, "realname")
        self.id_card = (By.NAME, "card_id")
        self.btn = (By.CSS_SELECTOR, '[value="确认提交"]')
        self.im_btn = (By.CSS_SELECTOR, ".btn.ng-scope")
        # 获取成功
        self.success_result = (By.CSS_SELECTOR, "body")
        # 获取失败
        self.fail_result = (By.CSS_SELECTOR, "#err > span")
    def open_account(self, name, id_card):
        """ 开户操作 """
        self.base_click(self.im_open)
        self.base_input(self.name, name)
        self.base_input(self.id_card, id_card)
        self.base_click(self.btn)
        self.base_click(self.im_btn)

    def get_suceess_result(self):
        """ 获取开户成功结果 """
        # 切换窗口
        return self.base_switch_handles(self.success_result).text
    
    def get_fail_result(self):
        """ 获取开户失败结果 """
        # 获取失败结果
        return self.fd_element(self.fail_result).text

if __name__ == '__main__':
    page = PageOpenAccount(Tools.get_driver())
    page.get_url()
    page.open_account("张三", "123456783256345678")
    print(page.suceess_result())