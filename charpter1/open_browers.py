#coding = utf-8
import requests
from selenium import webdriver
import json
import time
import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter1")
from read_init import ReadIni
from selenium.webdriver import except_conditions as EC
from selenium.webdriver.support import Select
from pykeyboard import PyKeyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from handle_json import handle_json

class SeleniumDriver():
    def __init__(self):
        self.driver = self.open_browser()

    def open_browser(self,open_browser):
        if open_browser == "chrome":
            options = webdriver.ChromeOptions()
            """
            @download.default_directory 下载路径
            @profile.default_directory_content_settings.popups 不弹出窗口
            """
            prefs = {'download.default_directory':"D:\Download\\",'profile.default_content_settings.popups':0}
            options.add_experimental_option('prefs',prefs)
            driver = webdriver.Chrome(chrome_options = options)
        if open_browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.download.dir',"D:\Download\\")
            profile.set_preference('browser.download.folderList',2)#1代表自身路径，2代表自定义路径
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/zip')#不过问任何下载配置
            driver = webdriver.Firefox(firefoxProfile = profile)
        if open_browser == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Edge()

    def get_url(self,url):
        self.driver.get(url)

    def close_driver(self):
        self.driver.close()

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

    def get_level_element(self,info):
        """
        层级定位
        有一个父节点
        父节点找子节点
        """
        element = self.get_element(info)
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

    def get_list_element(self,info):
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
                    self.click_element(info)
            else:
                if check == 'check':
                    self.click_element(info)             
        else:
            print("元素不可见,没办法选中")

    def get_local_element(self,info):
        readini = ReadIni()
        data = readini.get_value(info)
        data_info = data.split(">")
        return data_info

    def get_selected(self,info,value_index,index=None):
        """
        通过index获取我们selected，然后选择我们selected
        """
        selected_element = None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value_index)

    def upload_file(self,file_name):
        """
        非input上传文件
        @param filename
        """
        pykey = PyKeyboard()
        #pykey.tap_key(pykey.shift_key)
        pykey.type_string(file_name)
        pykey.type_key(pykey.enter_key)

    def upload_file_name_function(self,file_name,info,send_info=None):
        element = self.get_element(info)
        if element.tag_name == "a":
            #element = driver.find_element_by_xpath("//div[@class='showhide-search']/preceding-sibling::div[1]/input[1]")
            #self.get_element(info)
            self.send_value(send_info,file_name)
        else:
            self.click_element(info)
            self.upload_file(file_name)

    def download_file_canlendar(self,info):
        """
        下载文件
        """
        self.click_element(info)
    
    def js_excute(self,info):
        """
        执行js脚本
        """
        local = self.get_local_element(info)
        by = local[0]
        value = local[1]
        if by == 'id':
            by_key = 'getElementById'
            js = 'document.%s("%s").removeAttribute("readonly");'%(by_key,value)
        else:
            by_key = 'getElementsByClassName'
            js = 'document.%s("%s")[0].removeAttribute("readonly");'%(by_key,value)
        self.driver.js_excute(js)

    def calendar(self,info,value):
        """
        修改日历
        """
        element = self.get_element(info)
        try:
            element.get_attribute("readonly")
            self.js_excute_calendar(info)
        except:
            print("这个不是只读属性的日历")
        element.clear()
        self.send_value(info,value)
    
    def move_to_element(self,info):
        """
        移动鼠标到某个元素
        """
        element = self.get_element(info)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def refresh_F5(self):
        """
        强制刷新
        """
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
    
    def switch_iframe(self,info=None):
        """
        切换iframe
        """
        if info != None:
            iframe_element = self.get_element(info)
            self.driver.switch_to.frame(iframe_element)
        else:
            driver.switch_to.default_content()

    def switch_alert(self,info,value=None):
        """
        系统级弹窗
        @parame by info 确认or取消
        @parme by value 是否需要输入的值
        """
        window_alert = self.driver.switch_to.alert
        if info == "accept":
            if value == None:
                window_alert.accpet()
            else:
                window_alert.send_keys(value)
                window_alert.accpet()
        else:
            window_alert.dismiss()

    def scroll_get_element(self,list_info,str_info):
        """
        通过滚动条，滚动查找元素
        """
        T = True
        list_element = self.get_elements(list_info)
        js = "document.documentElement.scrollTop=100000;"
        while T:
            for element in list_element:
                course_name = element.find_element_by_tag_name("p").text
            if course_name in str_info:
                element.click()
                T = False
            driver.execute_script(js)

    def scroll_element(self,info):
        js = "document.documentElement.scrollTop=1000;"
        T = True
        while T:
            try:
                self.get_element(info)
                t = False
            except:
                driver.execute_script(js)

    def get_cookie(self):
    #接口
    #依赖
    
        cookie = self.driver.get_cookies()
        handle_json.write_data(cookie)

    def set_cookie(self):
        '''
        植入cookie
        '''
        cookie = handle_json.get_data()
        self.driver.delete_all_cookies()
        time.sleep(1)
        self.driver.add_cookie(cookie)
        time.sleep(2)

    def save_png(self):
        now_time = time.strftime("%Y%M%D.%H.%M.%S")
        self.driver.get_screenshot_as_file('%s.png' %now_time)

if __name__ == '__main__':
    request_driver = SeleniumDriver()
    # request_driver.get_url('https://www.imooc.com/user/newlogin')
    # request_driver.find_element_by_id("email")
    # request_driver.switch_windows("网站链接")

    # request_driver.get_element("id","username")
    # request_driver.send_value("element","test")
    request_driver.get_url("http://www.imooc.com/user/newlogin")
    #request_driver.send_value("name","email",1)
    # info = "username"
    # a = request_driver.get_element(info)
    # print(a)
    #request_driver.close_driver()
    