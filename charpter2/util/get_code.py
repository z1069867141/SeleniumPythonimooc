import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from PIL import Image
from util import ShowapiRequest
import time
import pytesseract

class Get_code(object):
    def __init__(self, driver):
        self.driver = driver

    """
    获取图片
    """
    def get_cod_img(self, file_name, file_name_1):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_elements_by_class_name("vm")[4]
        # print(code_element.location)
        # print(code_element.size)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        image = im.crop((left,top,right,height))
        image.save(file_name_1)

    """
    解析图片
    """
    def code_online(self, file_name, file_name_1):
        """
        selenium自己识别验证码
        """
        self.get_cod_img(file_name, file_name_1)
        image = Image.open(file_name_1)
        text = pytesseract.image_to_string(image)
        # print(text)
        # self. driver.find_element_by_name('seccodeverify').send_keys(text)
        time.sleep(2)
        return text

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.incnjp.com/member.php?mod=jionxc")
    a = Get_code(driver)
    a.code_online("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code1.png","C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\image\\code2.png")