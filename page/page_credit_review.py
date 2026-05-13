import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from selenium.webdriver.common.by import By
from base.page_base import BasePage

class PageCreditReview(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        # 默认frame元素
        self.loan_manger = (By.LINK_TEXT, "借款管理")
        self.limit_manger = (By.XPATH, "//span[text()='额度管理']")
        self.app_review = (By.LINK_TEXT, "额度申请审核")

        # frame1元素
        self.frame1 = (By.ID, "iframe_box")
        self.search_phone = (By.NAME, "member_name")
        self.search_btn = (By.CSS_SELECTOR, ".srcbtn")
        self.sele_rec = (By.XPATH, "//tbody/tr[1]/td[1]")
        self.review_btn = (By.XPATH, "//li[1]/a/span")

        # frame2元素
        self.frame2 = (By.ID, "xubox_iframe1")
        self.pass_btn = (By.XPATH, "//tbody/tr[5]/td[2]/div/label[1]/input")
        self.note = (By.XPATH, "//tbody/tr[6]/td[2]/div/textarea")
        self.im_code = (By.CSS_SELECTOR, ".mright-5.ng-pristine.ng-untouched.ng-valid.ng-scope")
        self.save_btn = (By.CSS_SELECTOR, ".dybtn.dybtn-save")

        # 通过
        self.app_rec = (By.LINK_TEXT, "额度申请记录")
        # self.status = (By.CSS_SELECTOR, "select[name='status']")
        self.status = (By.XPATH, "/html/body/div[2]/div[1]/div/ul/li[2]/div/select")
        self.rec_list = (By.CSS_SELECTOR, "body > div:nth-child(2) > div.info_list > table > tbody > tr:nth-child(1) > td.status > span")


    def menu_click(self):
           
        self.base_click(self.loan_manger)
        self.base_click(self.limit_manger)
        self.base_click(self.app_review)

    def search(self,phone):

        self.base_switch_frame(self.frame1)
        self.base_input(self.search_phone,phone)
        self.base_click(self.search_btn)


    def select_rec(self):
        time.sleep(2)
        self.base_click(self.sele_rec)
        self.base_click(self.review_btn)

    def review(self,note,im_code):
        self.base_switch_frame(self.frame2)
        self.base_click_p(self.pass_btn)
        self.base_input(self.note,note)
        self.base_input(self.im_code,im_code)
        self.base_click(self.save_btn)


    def application_review(self,phone,status="通过"):
       self.base_default_frame()
       self.base_click(self.app_rec)
       self.base_switch_frame(self.frame1)
       self.base_input(self.search_phone,phone)
       self.base_select(self.status,status)
       self.base_click(self.search_btn)

    def get_success_result(self):
        time.sleep(2)
        return self.fd_element(self.rec_list).text

