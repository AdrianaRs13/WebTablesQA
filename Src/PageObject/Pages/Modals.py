import sys

sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from Search.Src.PageObject.Locators import ModalsSM

class Modals(object):
    def __init__(self, driver):
        self.driver = driver
        self.small_button = driver.find_element(By.CSS_SELECTOR, ModalsSM.button_small)
        self.large_button = driver.find_element(By.CSS_SELECTOR, ModalsSM.button_large)

    def getModal(self, modalSelector):
        return self.driver.find_element(By.XPATH, modalSelector)

    def getElement(self, strSelector):
        return self.driver.find_element(By.CSS_SELECTOR, strSelector)


