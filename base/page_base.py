from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import PATH
import os
from tools import GetLog

class BasePage(object):
    """ 定位元素封装 """
    def __init__(self, driver, timeout=10):
        """ 初始化 """
        self.driver = driver
        self.default_timeout = timeout



    def fd_element(self,loc):
        """ 定位元素公共方法 """
        try: 
            element = WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f"元素定位失败：定位信息：{loc},错误详情{e})")
            raise


    def base_input(self, loc, text):
        """ 输入操作 """
        ele = self.fd_element(loc)
        ele.clear()
        ele.send_keys(text)


    def base_click(self, loc):
        """ 点击操作 """
        self.fd_element(loc).click()


    def get_host(self, file_name):
        """ 截图 """
        file_path = os.path.join(PATH, 'img',  file_name)
        self.driver.get_screenshot_as_file(file_path)


    def base_switch_handles(self, loc):
        """
        多窗口切换
        """
        # 获取所有窗口句柄
        WebDriverWait(self.driver, self.default_timeout).until(lambda x: len(x.window_handles) >= 2)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        # 在新窗口获取元素
        element = self.fd_element(loc)
        return element

    def base_switch_frame(self, loc):
        """
        切换到 iframe
        """
        # 等待frame加载完成并切换
        frame_ele = self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)

    def base_default_frame(self):
        """ 切回最外层默认frame """
        self.driver.switch_to.default_content()