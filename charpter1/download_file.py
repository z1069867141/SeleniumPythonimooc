from selenium import webdriver
import time

options = webdriver.ChromeOptions()
"""
@download.default_directory 下载路径
@profile.default_directory_content_settings.popups 不弹出窗口
"""
prefs = {'download.default_directory':"D:\Download\\",'profile.default_content_settings.popups':0}
options.add_experimental_option('prefs',prefs)

driver = webdriver.Chrome(chrome_options = options)
driver.get("https://www.imooc.com/mobile/app")
driver.find_elements_by_class_name("btn-download")[1].click()
time.sleep(2)
driver.close()