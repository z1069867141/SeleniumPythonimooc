import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from handle.register_handle import RegisterHandle
from PIL import Image

class RegisterBussiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, user, password, password_confirm, email, file_name, file_name_1):
        self.register_h.send_user_name(user)
        self.register_h.send_user_password(password)
        self.register_h.send_user_password_confirm(password_confirm)
        self.register_h.send_user_email(email)
        self.register_h.send_user_code(file_name, file_name_1)
        self.register_h.click_register_button

    def register_success(self):
        if self.register_h.click_register_text() == None:
            return True
        else:
            return False

    def register_function(self,username,password,password_confirm,email,file_name, file_name_1,assertelement,asserterrormessage):
        self.user_base(username, password, password_confirm, email, file_name, file_name_1)
        if self.register_h.get_error_text(assertelement, asserterrormessage) == None:
            print("检验不成功")
            return False
        else:
            return True

    # 执行操作:用户名输入错误
    def login_user_name_error(self, user, password, password_confirm, email, file_name, file_name_1):
        self.user_base(user, password, password_confirm, email, file_name, file_name_1)
        if self.register_h.get_error_text("user_name_error", "用户名不得小于\xa03\xa0个个字符") == None:
            print("检验不成功")
            return False
        else:
            return True

    # 执行操作:密码输入错误
    def login_password_error_element(self, user, password, password_confirm, email, file_name, file_name_1):
        self.user_base(user, password, password_confirm, email, file_name, file_name_1)
        if self.register_h.get_error_text("password_error", "请填写密码, 最小长度为 8 个字符") == None:
            print("检验不成功")
            return "False"
        else:
            return True

    # 执行操作：获取验证码图片
    def code_image(self):
        self.register_h.get_code_image()


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.incnjp.com/member.php?mod=jionxc")
    element_a = RegisterBussiness(driver)
    element_a.login_password_error_element("us123", "pw", "pw", "651651@qq.com","1564")
    # driver.find_element_by_id("email1y").send_keys("123")

