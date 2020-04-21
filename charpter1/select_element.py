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
time.sleep(2)
driver.get("https://www.imooc.com/user/setprofile")
driver.find_element_by_class_name("pull-right").click()
time.sleep(2)
driver.find_elements_by_class_name("moco-form-control")[7].find_elements_by_tag_name("option")[4].click()