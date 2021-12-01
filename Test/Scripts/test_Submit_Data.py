import sys
import time

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Search.Src.TestBase.WebDriverSetup import WebDriverSetup
from Search.Src.PageObject.Pages.TextBox import TextBox
from Search.Src.Utils.Utils import Utils
from Search.Src.PageObject.Locators import *


class Submit_Data(WebDriverSetup):
    def test_SubmitData(self):
        driver = self.driver
        self.driver.get("https://demoqa.com/text-box")
        Utils.page_is_loading(self.driver)

        name = 'Adri Rosas'
        email = 'adriana.rosas@email.com'
        caddress = 'Puebla, Mexico'
        paddress = 'Coatza, Veracruz'

        home = TextBox(driver)
        home.add_name.send_keys(name)
        home.add_email.send_keys(email)
        home.add_currentAddress.send_keys(caddress)
        home.add_permanentAddress.send_keys(paddress)

        Utils.waitUntilElementIsPresent(home.add_permanentAddress)

        home.submit_button.click()

        self.assertEqual(home.getElement(textBox.v_full_name).text, 'Name:' + name, "Name OK")
        self.assertEqual(home.getElement(textBox.v_email).text, 'Email:' + email, "Email OK")
        self.assertEqual(home.getElement(textBox.v_current_address).text, 'Current Address :' + caddress, "C Address OK")
        self.assertEqual(home.getElement(textBox.v_permanent_address).text, 'Permananet Address :' + paddress, "P Address OK")
        Utils.waitUntilElementIsPresent(home.getElement(textBox.v_full_name))


