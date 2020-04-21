from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://order.imooc.com/myorder")
driver.delete_all_cookies()

# driver.get("https://www.imooc.com/user/newlogin")
# email = driver.find_element_by_name("email")
# email.send_keys("18018845546")
# password = driver.find_element_by_name("password")
# password.send_keys("z54821348123")
# driver.find_element_by_class_name("moco-btn").click()
# time.sleep(2)
# cookie_list = driver.get_cookies()
# print(cookie_list)

cookie = {
        "domain": ".imooc.com", 
        "expiry": 1583083448, 
        "httpOnly": False, 
        "name": "apsid", 
        "path": "/", 
        "secure": False, 
        "value": "ZiNjI3MjM5ODkxZTY1Y2ZiMjI1YzNkNzM1YWE2NTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzkzNjg2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5MTk4MjQzNzBAcXEuY29tAAAAAAAAAAAAAAAAAAAAAGMzNzU2ZmU4OTAyNmMzMDBkNDBiNTFhZWIwMTVlMGYAKrFSXiqxUl4%3DZD"
}
time.sleep(2)
print(cookie)
driver.add_cookie(cookie)
time.sleep(2)
driver.get("https://order.imooc.com/myorder")
time.sleep(2)
driver.close()