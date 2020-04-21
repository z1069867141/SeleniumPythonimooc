from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.imooc.com/user/newlogin")
email = driver.find_element_by_name("email")
email.send_keys("18018845546")
password = driver.find_element_by_name("password")
password.send_keys("z54821348123")
driver.find_element_by_class_name("moco-btn").click()
time.sleep(5)

"""
查找元素返回数组
"""
driver.get("https://www.imooc.com/user/certificate")
elements = driver.find_elements_by_class_name("moco-form-control")
element_list = []
for element in elements:
    if element.is_displayed() == False:
        continue
    else:
        element_list.append(element)
print(element_list)
"""
检查文字是否存在
"""
# LOCATOR = (By.ID,"username")
# EC.visibility_of_element_located(LOCATOR)

"""
文字是否存在
"""
# driver.get("https://www.imooc.com/user/setprofile")
# driver.find_element_by_class_name("pull-right").click()
# element = driver.find_elements_by_name("email")[0].is_displayed()
# print(element)

# driver.find_element_by_class_name("test")
# driver.find_element_by_partial_link_text("Java").click()
# #driver.find_element_by_link_text("Java架构师体系课：跟随千万级项目从0到100全过程高效成长")
time.sleep(2)
#定位弹框元素
# driver.get("https://coding.imooc.com/class/402.html?mc_marking=b587280c0c1c0e76c1092aa21406565a&mc_channel=syb6")
# driver.find_elements_by_class_name("js-addcart")[0].click()
# time.sleep(4)
# driver.find_element_by_class_name("btn-close").click()
# time.sleep(2)
#定位imooc的猿问
# driver.get("https://www.imooc.com/wenda/save")
# time.sleep(3)
# driver.switch_to_active_element().send_keys("test")
# time.sleep(10)

#标签（input） id（#） class（.）
#driver.find_elements_by_css_selector(".icon-search")

# driver.get("https://www.imooc.com/user/setprofile")
# driver.find_element_by_class_name("pull-right").click()
# driver.find_elements_by_xpath("//input[@id='nick']")[1].send_keys("1")
# time.sleep(5)

driver.close()