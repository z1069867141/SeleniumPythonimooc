import ddt
import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from business.register_bussiness import RegisterBussiness
from selenium import webdriver
import HTMLTestRunner
import unittest
import os 

@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这个是setup")
    
    def tearDown(self):
        print("这个是teardown")

    @ddt.data(
        ['1','2'],
        ['3','4'],
        ['5','6']
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)

if __name__ == "__main__":
    unittest.main()