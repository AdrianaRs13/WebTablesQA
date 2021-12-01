import sys
import time

sys.path.append(sys.path[0] + "/...")

import unittest
from time import sleep
from Search.Src.TestBase.WebDriverSetup import WebDriverSetup
from Search.Src.PageObject.Pages.Modals import Modals
from Search.Src.Utils.Utils import Utils
from Search.Src.PageObject.Locators import *

class Modals_SM(WebDriverSetup):

    def test_CierraName(self):
        driver = self.driver
        self.driver.get("https://demoqa.com/modal-dialogs")
        Utils.page_is_loading(self.driver)

        home = Modals(driver)

        home.small_button.click()
        home.webModal = home.getModal(ModalsSM.modal)
        Utils.waitUntilElementIsPresent(home.webModal)
        home.CloseSModal = home.getElement(ModalsSM.buttonC_small)
        home.CloseSModal.click()
        time.sleep(1.5)

        home.large_button.click()
        home.webModal = home.getModal(ModalsSM.modal)
        Utils.waitUntilElementIsPresent(home.webModal)
        home.CloseLModal = home.getElement(ModalsSM.buttonC_large)
        home.CloseLModal.click()
        Utils.waitUntilElementIsPresent(home.CloseLModal)


if __name__ == '__main__':
    unittest.main()