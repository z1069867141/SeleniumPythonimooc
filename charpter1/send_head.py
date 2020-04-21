from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pykeyboard import PyKeyboard

driver = webdriver.Chrome()
pykey = PyKeyboard()
driver.get("chrome://settings/importData")
# driver.get("https://www.imooc.com/user/newlogin")
# email = driver.find_element_by_name("email")
# email.send_keys("18018845546")
# password = driver.find_element_by_name("password")
# password.send_keys("z54821348123")
# driver.find_element_by_class_name("moco-btn").click()
# time.sleep(2)
# driver.get("https://www.imooc.com/user/setprofile")
# time.sleep(2)
# driver.find_element_by_class_name("update-avator").click()
# driver.find_elements_by_id("uypload").send_keys("输入图片地址")
pykey.tap_key(pykey.shift_key)
time.sleep(3)
pykey.type_string("asddasd")
pykey.type_key(pykey.enter_key)
time.sleep(3)
driver.close()