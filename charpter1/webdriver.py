#coding = utf-8
from selenium import webdriver
import time,errno
from selenium.webdriver.support import expected_conditions as EC
#类使用


class SeleniumDriver():
    def __init__(self,browser):
            self.driver = self.open_browser(browser)

    def open_browser(self,browser):
        try:
            if browser == "chrome":
                driver = webdriver.Chrome()
            elif browser == "firefox":
                driver = webdriver.Firefox()
            elif browser == "ie":
                driver = webdriver.Ie()
            else:
                driver =webdriver.Edge()
            time.sleep(2)
            return driver
        except:
            print("打开浏览器失败")
            return None

    def get_url(self,url):
        if self.driver != None:
            if "https://" in url:
                self.driver.get(url)
            else:
                print("你的url有问题")
        else:
            print("case失败")

    def handle_windows(self,*args):
        value = len(args)
        if value == 1:
            if args[0] == "max":
                self.driver.maximize_window()
            elif args[0] == "refresh":
                self.driver.refresh()
            elif args[0] == "back":
                self.driver.back()
            elif args[0] == "forward":
                self.driver.forward()
            else:
                self.driver.minimize_window()
        elif value == 2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print("输入信息有误")
        time.sleep(5)
        self.driver.quit()

    def assert_title(self,title_name=None):
        """
        判断title是否正确
        """
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self,url,title_name=None):
        self.get_url(url)
        return self.assert_title(title_name)

    def close_driver(self):
        self.driver.quit()

    def switch_windows(self,title = None):
        """
        切换windows窗口
        """
        handl_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in handl_list:
            if i != current_handle:
                time.sleep(1)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break

        time.sleep(2)
        self.driver.find_element_by_id("userId").send_keys("test")
        time.sleep(2)

if __name__ == "__main__":
    Selenium_driver = SeleniumDriver("chrome")
    Selenium_driver.open_url_is_true("https://www.imooc.com/","程序员")
    time.sleep(5)
    Selenium_driver.switch_windows("慕课网")
    Selenium_driver.close_driver()
    #Selenium_driver.handle_windows("max")
    #get_url("https://www.imooc.com/")
    #handle_windows("forward") #max,refresh,back,forward,(200,300)
