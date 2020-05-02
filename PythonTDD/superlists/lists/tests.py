from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\PythonTDD\\superlists")
from lists.views import home_page
from django.template.loader import render_to_string
from django.test import TestCase

class HomePageTest(TestCase):
        def  test_user_home_template(self):
            response = self.client.get("/")
            self.assertTemplateUsed(response,"home.html")