from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

    # 获取用户名元素
    def get_user_name_element(self):
        return self.fd.get_element("user_name")
        # 通过assert判断是否未error

    # 获取用户名报错元素
    def get_user_name_error_elmenet(self):
        return self.fd.get_element("user_name_error")

    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_element("password")

    # 获取密码报错元素
    def get_password_error_element(self):
        return self.fd.get_element("password_error")

    # 获取确认密码元素
    def get_user_password_confirm_element(self):
        return self.fd.get_element("password_confirm")

    # 获取确认密码报错元素
    def get_user_password_confirm_error_element(self):
        return self.fd.get_element("password_confirm_error")

    # 获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("email")

    # 获取邮箱报错元素
    def get_email_error_element(self):
        return self.fd.get_element("email_error")

    # 获取输入验证码图片元素
    def get_user_image_element(self):
        return self.fd.get_element("code_image")

    # 获取输入验证码元素
    def get_user_code_element(self):
        return self.fd.get_element("seccodeverify")

    # 获取输入验证码错误元素
    def get_user_code_error_element(self):
        return self.fd.get_element("seccodeverify_Verification_errorcode")

    # 获取注册按钮元素
    def get_register_button(self):
        return self.fd.get_element("button")