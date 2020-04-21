from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC #预期条件包
from selenium.webdriver.support.select import Select #选择下拉框
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import random
from PIL import Image
import sys
sys.path.append("C:/Users/Akien/Desktop/测试练习笔记/自动化/charpter2")
from imooc_selenium.ShowapiRequest import ShowapiRequest
import pytesseract

driver = webdriver.Chrome()
driver.get("https://www.incnjp.com/member.php?mod=jionxc")
a = EC.title_contains("注册")#包含title
print(a(driver))
driver.find_element_by_class_name("pn").click()

# """
# 如何生成随机用户名
# """
# email_element = driver.find_element_by_id("username3d")
# for i in range(5):
#     user_email = random.sample("123456789abcdefg",10)
#     user_email_value = "".join(user_email)
#     print(user_email_value)

"""
截取验证码
"""
driver.save_screenshot("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code.png")
code_element = driver.find_elements_by_class_name("vm")[4]
print(code_element.location)
print(code_element.size)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code.png")
image = im.crop((left,top,right,height))
image.save("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code1.png")

"""
selenium自己识别验证码
"""
image = Image.open("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code1.png")
text = pytesseract.image_to_string(image)
print(text)
driver.find_element_by_name('seccodeverify').send_keys(text)


"""
第三方api识别验证码
https://www.showapi.com/apiGateway/view?apiCode=1274
# """
# r = ShowapiRequest("http://route.showapi.com/1274-2","152723","6bf4ca3f0b344e0d82fb920553cc1230" )
# r.addFilePara("imgFile", r"C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code1.png")
# res = r.post()
# text = res.json()["showapi_res_body"]["texts"][0]
# print(text) # 返回信息
# time.sleep(2)
# driver.find_elements_by_class_name("seccodeverify_cSWK6YQS").send_keys(text)

""" 
监测信息是否包含
"""
# locator = (By.CLASS_NAME,"pn")
# WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

"""
# 查询输入框内的值，不论是默认的还是自己输入的
"""
# password_element = driver.find_element_by_id("password7g")
# password_element.send_keys("z54821348123")
# print(password_element.get_attribute("value"))#搜索输入信息

# # b = EC.title_is("注册")#等于title
# # print(b(driver))
# driver.find_element_by_class_name("pn").click()
# time.sleep(2)
# driver.find_element_by_id("username3d").send_keys("z1069867141")
# driver.find_element_by_id("password7g").send_keys("z1069867141")
# driver.find_element_by_id("password5w").send_keys("z1069867141")
# driver.find_element_by_id("email1y").send_keys("z1069867141@qq.com")
# select_element = driver.find_element_by_id("nationality")
# Select(select_element).deselect_by_value("中国")