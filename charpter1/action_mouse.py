from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.imooc.com/")
element = driver.find_elements_by_class_name("menuContent").find_elements_by_class_name("item")[0]
ActionChains(driver).move_to_element(element).perform()
driver.find_elements_by_class_name("tag-box")[1].find_element_by_link_text("前端工具").click()
time.sleep(2)
driver.close()