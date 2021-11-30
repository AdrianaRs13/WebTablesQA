import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
from time import sleep
from selenium.webdriver.common.by import By
from Search.Src.PageObject.Locators import Locator



class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element(By.CSS_SELECTOR, Locator.logo)
        self.search_text = driver.find_element(By.XPATH, Locator.search_text)
        self.submit = driver.find_element(By.XPATH, Locator.submit)

    def getSearchText(self):
        return self.search_text

    def getSubmit(self):
        return self.submit

    def getWebPageLogo(self):
        return self.logo