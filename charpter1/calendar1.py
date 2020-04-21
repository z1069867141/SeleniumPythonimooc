from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://fanrongdemo.qianyansoft.com/Admin/Orders/pageList/type/b2c.html")
driver.find_elements_by_class_name("iptTxt")[0].send_keys("admin")
driver.find_elements_by_class_name("iptTxt")[1].send_keys("qyadmin")
time.sleep(4)
js = 'document.getElementById("finder_buttonA").removeAttribute("readonly");'
driver.execute_script(js)
element = driver.find_elements_by_class_name("finder_buttonA")[1]
element.clear()
element.send_keys("2020-2-14")
time.sleep(4)