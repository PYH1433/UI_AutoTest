import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pytest
from tools import Tools
from page.page_login import PageLogin
from page.page_register import PageRegister
from page.page_open_account import PageOpenAccount


@pytest.fixture()
def driver():
    """ 获取driver """
    dri = Tools.get_driver()
    yield dri
    Tools.quit_driver()

@pytest.fixture()
def pg_login(driver):
    """ 登录 """
    pg_login = PageLogin(driver)
    pg_login.get_url()
    return pg_login

@pytest.fixture()
def pg_register(driver):
    """ 注册 """
    pg_register = PageRegister(driver)
    pg_register.get_url()
    return pg_register


@pytest.fixture()
def open_acc(driver,pg_login):
    """ 开通账户 """ 
    pg_login.login("13640175555","123abc")
    open_acc = PageOpenAccount(driver)
    return open_acc


    