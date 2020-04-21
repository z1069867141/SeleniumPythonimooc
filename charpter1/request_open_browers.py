#coding = utf-8
import requests
import json
import time
import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化")
from charpter1.read_init import ReadIni

class SeleniumDriver():
    def __init__(self):
        self.driver = self.chrome_driver()

    def chrome_driver(self):
        url = 'http://127.0.0.1:4444/wd/hub/session/'
        data = json.dumps({
            'desiredCapabilities':{
                'browserName':'chrome'
            }
        })
        res = requests.post(url,data).json()
        session = res['sessionId']
        driver = url + session
        return driver

    def get_url(self,url):
        base_url = self.driver + '/url'
        data = json.dumps({
            'url':url
        })
        requests.post(base_url,data)

    def close_driver(self):
        self.driver.close()

    def find_element_by_id(self,value):
        base_url = self.driver + '/element'
        data = json.dumps({
            'using':'name',
            'value':value
        })
        res = requests.post(base_url,data).json()['value']['element-6066-11e4-a52e-4f735466cecf']
        return res

    def switch_windows(self,title_name=None):
        handle_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in handle_list:
            if i != current_handle:
                time.sleep(2)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break

        time.sleep(5)
        self.driver.find_element_by_id("userId").send_keys("test")

    def get_element(self,info):
        """
        获取元素element
        @parme by 定位方式
        @parme value 定位置
        @return 返回一个元素
        """
        element = None
        by,value = self.get_local_element(info)
        #self.driver.find_element_by_name("email")
        #try:
        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "css":
            element = self.driver.find_element_by_css(value)
        elif by == "class":
            element = self.driver.find_element_by_class(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        #except:
            #print("定位by和value有问题")
        return element

    def get_elements(self,info):
        """
        获取元素elements
        @parme by 定位方式
        @parme value 定位置
        @return 返回一个元素
        """
        elements = None
        by,value = self.get_local_element(info)
        element_list = []
        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class(value)
        elif by == "xpath":
            elements = self.driver.find_elements_by_xpath(value)
        for element in elements:
            if self.element_isdisplay(elements) == False:
                continue
            else:
                element_list.append(element)
        return self.element_isdisplay(elements)  

    def element_isdisplay(self,element):
        flag = element.is_displayed()
        if flag == True:
                return element
        else:
            return False

    def get_level_element(self,info_level,node_info):
        """
        层级定位
        有一个父节点
        父节点找子节点
        """
        element = self.get_element(info_level)
        node_by,node_value = self.get_local_element(info)
        if element == False:
            return False
        if node_by == "id":
            node_element = element.find_element_by_id(node_value) 
        elif node_by == "name":
            node_element = element.find_element_by_name(node_value)
        elif node_by == "css":
            node_element = element.find_element_by_css(node_value)
        elif node_by == "class":
            node_element = element.find_element_by_class(node_value)
        elif node_by == "xpath":
            node_element = element.find_element_by_xpath(node_value)
        return self.element_isdisplay(element)  

    def get_list_elements(self,info):
        """
        通过list定位我们的元素
        """
        elements = self.get_elements(info)
        index = 0
        if index > len(elements):
            return None
        return self.element_isdisplay(elements[index])

    def send_value(self,info,key):
        """
        输入值
        """
        element = self.get_element(info)
        if element == False:
            print("输入失败，定位元素没有展现")
        else:
            if element != None:
                element.send_keys(key)
            else:
                print("输入失败，定位元素没有找到")

    def click_element(self,info):
        """
        点击元素
        """
        element = self.get_element(info)
        if element != False:
            if element != None:
                element.click()
            else:
                print("点击失败，定位元素没有找到")
        else:
            print("点击失败，元素不可见")

    def check_box_isselected(self,info,check=None):
        """
        选中
        """
        element = self.get_elements(info)
        if element != False:
            flag = element.is_selected()
            if flag == True:
                if check != 'check':
                    self.click_element(by,value)
            else:
                if check == 'check':
                    self.click_element(by,value)             
        else:
            print("元素不可见,没办法选中")

    def get_local_element(self,info):
        data = read_ini.get_value(info)
        data_info = data.split(">")
        return data_info

if __name__ == '__main__':
    request_driver = SeleniumDriver()
    # request_driver.get_url('https://www.imooc.com/user/newlogin')
    # request_driver.find_element_by_id("email")
    # request_driver.switch_windows("网站链接")

    # request_driver.get_element("id","username")
    # request_driver.send_value("element","test")
    request_driver.get_url("http://www.imooc.com/user/newlogin")
    #request_driver.send_value("name","email",1)
    request_driver.get_element("name","email")
    request_driver.close_driver()