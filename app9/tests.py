from django.test import TestCase, Client
from django.urls import resolve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from .views import home
import time


#Create your tests here.

## -------------------------------------- Unit Test ----------------------------------------
class Story9Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)
    
    def test_story9_using_home_func(self):
        found = resolve('/')
        self.assertEqual(found.func, home)