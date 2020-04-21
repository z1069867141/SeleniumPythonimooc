from selenium import webdriver
from base.find_element import FindElement
from util.get_code import Get_code
from selenium.webdriver.support.select import Select
import time

class ActionMethod(object):
    def __init__(self):
        pass

    def open_browser(self,browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        else:    
        #elif browser == "firefox":
            self.driver = webdriver.Firefox()
        # else:
        #     self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self,url):
        self.driver.get(url)

    # 获取网页title
    def get_title(self):
        return self.driver.title

    # 定位元素
    def get_element(self,element):
        find_element = FindElement(self.driver)
        element = find_element.get_element(element)
        return element

    # 输入元素
    def element_send_keys(self,element,value):
        element = self.get_element(element)
        element.send_keys(value)

    # 点击元素
    def click_element(self,element):
        self.get_element(element).click()

    # 选择下拉框内容
    def select_value(self,element,value):
        select_element = self.get_element(element)
        Select(select_element).select_by_value(value)

    # 输入验证码
    def seccodeverify(self,element):
        code = Get_code(self.driver)
        text = code.code_online("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code1.png","C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code2.png")
        self.get_element(element).send_keys(text)

    def sleep_time(self,s_time):
        time.sleep(int(s_time))

    def close_browser(self):
        self.driver.close()