import sys

sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from Search.Src.PageObject.Locators import textBox


class WebTablesPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.add_name = driver.find_element(By.CSS_SELECTOR, textBox.full_name)
        self.add_email = driver.find_element(By.CSS_SELECTOR, textBox.email)
        self.add_currentAddress = driver.find_element(By.CSS_SELECTOR, textBox.current_address)
        self.add_permanentAddress = driver.find_element(By.CSS_SELECTOR, textBox.permanent_address)

    def getFullName(self):
        return self.add_name

    def getEmail(self):
        return self.add_email

    def getCurrentAddress(self):
        return self.add_currentAddress

    def getPermanentAddress(self):
        return self.add_permanentAddress

