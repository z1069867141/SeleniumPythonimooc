import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from page.register_page import RegisterPage
from util.get_code import Get_code
from PIL import Image

class RegisterHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # 输入邮箱
    def send_user_name(self, user_name):
        self.register_p.get_user_name_element().send_keys(user_name)

    # 输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入确认密码
    def send_user_password_confirm(self, password_confirm):
        self.register_p.get_user_password_confirm_element().send_keys(password_confirm)

    # 输入邮箱
    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    # 输入验证码
    def send_user_code(self, file_name, file_name_1):
        get_code_text = Get_code(self.driver)
        code = get_code_text.code_online(file_name,file_name_1)
        self.register_p.get_user_code_element().send_keys(code)

    # # 获取验证码图片
    # def get_code_image(self):
    #     self.driver.save_screenshot("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code.png")
    #     code_element = self.register_p.get_user_image_element()
    #     left = code_element.location['x']
    #     top = code_element.location['y']
    #     right = code_element.size['width']+left
    #     height = code_element.size['height']+top
    #     im = Image.open("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code.png")
    #     image = im.crop((left,top,right,height))
    #     image.save("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code1.png")

    # 获取错误信息
    def get_error_text(self, info, user_info):
        # try:
        if info == "user_name_error":
            message = self.register_p.get_user_name_error_elmenet().text
            # if message == user_info:
            #     message
            # else:
            #     message = None
        elif info == "password_error":
            message = self.register_p.get_password_error_element().text
            # if message == user_info:
            #     message
            # else:
            #     message = None
        else:
            pass
        # except:
        #     text = None
        return message

    # 注册按钮
    def click_register_button(self):
        self.register_p.get_register_button_element().click()

    # 检测点击注册之后，是否有注册页面的元素存在
    def click_register_text(self):
        self.register_p.get_register_button_element().text


if __name__ == "__main__":
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get("https://www.incnjp.com/member.php?mod=jionxc")
    element_a = RegisterHandle(driver)
    element_a.get_code_image()
    # time.sleep(5)
    # element_a.get_error_text("password_error","请填写密码, 最小长度为 8 个字符")
    # driver.find_element_by_id("email1y").send_keys("123")
