from features.lib.page.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    def __init__(self,context):
        super().__init__(context.driver)
    
    def send_register(self):
        self.find_element(By.id,"")