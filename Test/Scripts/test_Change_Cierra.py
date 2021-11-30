import sys
import time

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Search.Src.TestBase.WebDriverSetup import WebDriverSetup
from Search.Src.PageObject.Pages.WebTablesPage import WebTablesPage
from Search.Src.Utils.Utils import Utils
from Search.Src.PageObject.Locators import *


class Change_Cierra(WebDriverSetup):

    def test_CierraName(self):
        driver = self.driver
        self.driver.get("https://demoqa.com/webtables")
        Utils.page_is_loading(self.driver)

        home = WebTablesPage(driver)

        # home.search_text.send_keys("Cierra")
        # self.assertEqual(home.cierra_name.text, 'Cierra', "Name Found")
        # time.sleep(3)

        home.edit_button.click()
        home.webModal = home.getElement(webTable.modal)
        Utils.waitUntilElementIsPresent(home.webModal)

        home.webName = home.getElement(webTable.input_name)
        home.webName.clear()
        home.webName.send_keys("Adri")
        Utils.waitUntilElementIsPresent(home.webName)

        home.webSubmit= home.getElement(webTable.submit_button)
        home.webSubmit.click()
        time.sleep(2)

        home.search_text.send_keys("Adri")
        self.assertEqual(home.cierra_name.text, 'Adri', "Name Found")



if __name__ == '__main__':
    unittest.main()