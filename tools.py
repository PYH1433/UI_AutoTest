import json
import logging
import time
from selenium import webdriver 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from config import PATH


class Tools:
    """ 浏览器驱动类 """

    driver = None

    @classmethod
    def get_driver(cls):
        """ 获取浏览器驱动 """
        if cls.driver is None:
            path = r"D:\tool\conda\azlj\msedgedriver.exe"
            ser = Service(executable_path=path)  
            cls.driver = webdriver.Edge(service=ser)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver


    @classmethod
    def quit_driver(cls):
        """ 退出浏览器 """
        if cls.driver:
            time.sleep(2)
            cls.driver.quit()
            cls.driver = None


    def read_json(file_name):
        """ 读取json文件 """
        data = []
        file_path = PATH + "/data/" + file_name
        with open(file_path, "r", encoding="utf-8") as f:
            tmp = json.load(f)
            for i in tmp:
                a = tuple(i.values())
                data.append(a)
            return data


class GetLog:
        # 日志器
        __log = None

        def get_log(cls):
            if cls.__log is None:
                # 创建日志器
                cls.__log = logging.getLogger()
                # 设置日志级别
                cls.__log.setLevel(logging.INFO)
                # 创建处理器
                filename = PATH + "/log/" + "Web.log"
                tf = logging.handles.TimedRotatingFileHandler(filename=filename, 
                                                                when="midnight",
                                                                interval=1,
                                                                backupCount=3, 
                                                                encoding="utf-8")
                fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
                fm = logging.Formatter(fmt)
                tf.setFormatter(fm)
                cls.__log.addHandler(tf)
            return cls.__log




    