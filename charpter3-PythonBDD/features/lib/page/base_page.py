from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        pass

    # 打开网页
    def get_url(self,url):
        self.driver.get(url)

    # 获取标题
    def get_title(self):
        return self.driver.title

    # 获取元素
    def find_element(self,*loc):
        self.driver.find_element(By.id,"")