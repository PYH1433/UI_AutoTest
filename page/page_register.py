import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By
from config import BASE_URL
from base.page_base import BasePage


class PageRegister(BasePage):
    """ 注册页面 """
    
    def __init__(self,driver):
        super().__init__(driver)
        """ 注册页面元素定位 """
        self.phone = (By.ID, "phone")
        self.password = (By.ID, "password")
        self.img_code = (By.ID, "verifycode")
        self.get_phone_code = (By.ID, "get_phone_code")
        self.phone_code = (By.ID, "phone_code")
        self.reg = (By.CLASS_NAME, "lg-btn")
        # 成功注册元素定位
        self.success_result = (By.CSS_SELECTOR,"#step3 > div > div > h1")
        # 注册失败元素定位
        self.fail_result = (By.CLASS_NAME,"reg-title")


    def get_url(self):
        """ 访问注册页面 """
        self.driver.get(BASE_URL + "/common/member/reg")

    def register(self, phone, password, img_code, phone_code):
        """ 注册操作 """
        # 输入手机号
        self.base_input(self.phone, phone)
        # 输入密码
        self.base_input(self.password, password)
        # 输入图片验证码
        self.base_input(self.img_code, img_code)
        # 点击获取手机验证码
        self.base_click(self.get_phone_code)
        # 输入手机验证码
        self.base_input(self.phone_code, phone_code)
        # 点击注册
        self.base_click(self.reg)

    def get_success_result(self):
        """ 获取注册成功结果 """
        return self.fd_element(self.success_result).text


    def get_fail_result(self):
        """ 获取注册失败结果 """
        return self.fd_element(self.fail_result).text



# if __name__ == '__main__':
#     p1 = PageRegister(Tools.get_driver())
#     p1.get_url()
#     p1.register("12115122391","123abc",8888,666666)