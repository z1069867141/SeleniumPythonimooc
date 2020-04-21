from selenium import webdriver
import time
import random
from PIL import Image
import pytesseract

driver = webdriver.Chrome()

"""
初始化浏览器
"""
def driver_init():
    driver.get("https://www.incnjp.com/member.php?mod=jionxc")
    driver.maximize_window()#最大化窗口
    time.sleep(2)

"""
获取element信息
"""
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

"""
如何生成随机用户名
"""
def get_range_user():
    user_info = ''.join(random.sample("123456789abcdefg",10))
    return user_info

"""
获取图片
"""
def get_cod_img(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_elements_by_class_name("vm")[4]
    # print(code_element.location)
    # print(code_element.size)
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top
    im = Image.open(file_name)
    image = im.crop((left,top,right,height))
    image.save(file_name)

"""
解析图片
"""
def code_online(file_name):
    """
    selenium自己识别验证码
    """
    image = Image.open(file_name)
    text = pytesseract.image_to_string(image)
    print(text)
    driver.find_element_by_name('seccodeverify').send_keys(text)

"""
运行主程序
"""
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"163@.com"
    driver_init()
    file_name = "C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code1.png"
    get_element("username3d").send_keys(user_name_info)
    get_element("password7g").send_keys("z54821348123")
    get_element("password5w").send_keys("z54821348123")
    get_element("email1y").send_keys(user_email)
    get_element("nationality").deselect_by_value("中国")
    get_cod_img(file_name)
    text = code_online(file_name)
    get_element("seccodeverify").send_keys(text)
    get_element("registerformsubmit").click()
    driver.close()

run_main()