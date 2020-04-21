import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化")
from charpter1.read_init import ReadIni
from charpter1.request_open_browers import SeleniumDriver
a = "./config/LocalElement.ini"
read_ini = ReadIni(a)
data = read_ini.get_value("element","username")

Selenium_driver = SeleniumDriver()

data_info = data.split(">")
by = data_info[0]
local = data_info[1]
print(by,"---->",local)
Selenium_driver.get_url("http://www.imooc.com/user/newlogin")
Selenium_driver.send_value(by,local,"Akien")