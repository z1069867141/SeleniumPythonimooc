import ddt
import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from business.register_bussiness import RegisterBussiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import HTMLTestRunner
import unittest
import os 

ex = ExcelUtil()
data = ex.get_data()

# 用户名，密码，确认密码，邮箱，验证码路径，错误信息定位元素，错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.incnjp.com/member.php?mod=jionxc")
        self.driver.save_screenshot("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\test1.png")
        self.login = RegisterBussiness(self.driver)


    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # @ddt.data(
    #         ['12','z54821348123','z54821348123','123561@qq.com',
    #         'C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code1.png',
    #         'C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code2.png',
    #         'user_name_error','用户名不得小于 3 个字符'],
    #         ['1234567','z54821348123','z54821348123','123561@qq.com',
    #         'C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code1.png',
    #         'C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code2.png',
    #         'user_name_error','用户名不得小于 3 个字符']
    #     )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self,data):
        username,password,comfirmpd,email,file_name,file_name_1,assertelement,asserterrormessage = data
        user_error = self.login.register_function(username,password,comfirmpd,email,file_name,file_name_1,assertelement,asserterrormessage)
        return self.assertTrue(user_error,"此条case成功")

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case1.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description="这个是我们第一次报告1", verbosity = 2)
    runner.run(suite)