import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from util.read_ini import ReadIni
from selenium import webdriver

class FindElement(object):

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        data_list = data.split(">")
        # print(data_list)
        by = data_list[0]
        # print(by)
        value = data_list[1]
        # print(value)
        No = 0
        if by=="classnames":
            No = int(data_list[2])
    
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "classname":
                return self.driver.find_element_by_class_name(value)
            elif by == "classnames":
                return self.driver.find_elements_by_class_name(value)[No]
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except:
            self.driver.save_screenhot()
            return None


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.incnjp.com/member.php?mod=jionxc")
    element_a = FindElement(driver)
    element_a.get_element("password").send_keys("123")
    element_a.get_element("register_button").click()
    text = element_a.get_element("password_error").text
    print(text)
    # driver.find_element_by_id("email1y").send_keys("123")