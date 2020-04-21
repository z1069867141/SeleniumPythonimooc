import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from business.register_bussiness import RegisterBussiness
from selenium import webdriver
from log.user_log import userlog
import HTMLTestRunner
import unittest
import os 

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = "C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code1.png"#保存含有验证码的图片
        cls.file_name_1 = "C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code2.png"#保存验证码图片
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.incnjp.com/member.php?mod=jionxc")
        self.driver.save_screenshot("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\test1.jpg")
        self.login = RegisterBussiness(self.driver)
        self.logger.info("this is Chrome")


    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_user_name_error(self):
        user_error = self.login.login_user_name_error("us", "pw111", "pw111", "651651@qq.com",self.file_name, self.file_name_1)
        a = self.assertTrue(user_error,"此条case成功")
        
        # if user_error == True:
        #     print("注册失败，此条case成功")
        # 通过assert判断是否未error

    def test_user_password(self):
        user_error = self.login.login_password_error_element("us123", "pw", "pw", "651651@qq.com",self.file_name)
        a = self.assertTrue(user_error,"此条case成功")

    def test_user_password_confirm(self):
        print("2")
        pass

    def test_user_email(self):
        print("3")
        pass

    def test_user_code(self):
        print("4")
        pass

    def test_login_success(self):
        print("5")
        success = self.login.user_base("user111", "pw111", "pw111", "651651@qq.com")
        self.assertFalse(success,"此条case成功")
        # if success == True:
        #     print("注册成功")


# def main():
#     first = FirstCase()
#     first.test_user_name_error()


if __name__ == "__main__":
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case.html")
    f = open(file_path,'wb')
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_user_name_error"))
    # suite.addTest(FirstCase("test_user_password"))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first case",description="这个是我们第一次报告", verbosity = 2)
    runner.run(suite)
    import time
    time.sleep(10)