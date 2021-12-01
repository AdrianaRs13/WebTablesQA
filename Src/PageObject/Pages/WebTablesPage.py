import sys

sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from Search.Src.PageObject.Locators import webTable


class WebTablesPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.edit_button = driver.find_element(By.CSS_SELECTOR, webTable.edit_button)
        self.cierra_name = driver.find_element(By.XPATH, webTable.cierra_name)
        self.search_text = driver.find_element(By.XPATH, webTable.search_text)
        # self.modal = driver.find_element(By.XPATH, webTable.modal)
        # self.input_name = driver.find_element(By.XPATH, webTable.input_name)
        # self.submit_button = driver.find_element(By.XPATH, webTable.submit_button)


    def getSearchText(self):
        return self.search_text

    def getCierraName(self):
        return self.cierra_name

    def getEditButton(self):
        return self.edit_button

    def getModal(self):
        return self.modal

    def getInputName(self):
        return self.input_name

    def getSubmitButton(self):
        return self.submit_button

    def getElement(self, strSelector):
        return self.driver.find_element(By.XPATH, strSelector)
