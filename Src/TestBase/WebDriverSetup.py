import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3
from selenium.webdriver.support.ui import WebDriverWait


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            #sleep(2)
            self.driver.close()
            self.driver.quit()

