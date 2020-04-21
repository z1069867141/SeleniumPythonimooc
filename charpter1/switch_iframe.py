from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.imooc.com/user/newlogin")
email = driver.find_element_by_name("email")
email.send_keys("18018845546")
password = driver.find_element_by_name("password")
password.send_keys("z54821348123")
driver.find_element_by_class_name("moco-btn").click()
time.sleep(2)
driver.get("https://www.imooc.com/wenda/save")
time.sleep(2)
driver.switch_to.frame("ueditor_0")

p_element = driver.find_element_by_tag_name("p")
ActionChains(driver).move_to_element(p_element).click().send_keys("test").perform()
driver.switch_to.default_content()

driver.find_elements_by_class_name("save-list-tag")[1].click()

time.sleep(2)
#driver.close()