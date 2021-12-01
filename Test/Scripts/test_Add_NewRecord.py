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

class New_Record(WebDriverSetup):

    def test_CierraName(self):
        driver = self.driver
        self.driver.get("https://demoqa.com/webtables")
        Utils.page_is_loading(self.driver)

        home = WebTablesPage(driver)

        home.add_button.click()
        home.webModal = home.getElement(webTable.modal)
        Utils.waitUntilElementIsPresent(home.webModal)

        name = 'Susana'
        lastname = 'Diaz'
        email = 'sdiaz23@hotmail.com'
        age = '23'
        salary = '12000'
        department = 'Decor&Design'

        home.writeName = home.getElementCSS(webTable.input_name)
        home.writeLName = home.getElementCSS(webTable.input_lastname)
        home.writeEmail = home.getElementCSS(webTable.input_email)
        home.writeAge = home.getElementCSS(webTable.input_age)
        home.writeSalary = home.getElementCSS(webTable.input_salary)
        home.writeDepartment = home.getElementCSS(webTable.input_department)

        home.writeName.send_keys(name)
        home.writeLName.send_keys(lastname)
        home.writeEmail.send_keys(email)
        home.writeAge.send_keys(age)
        home.writeSalary.send_keys(salary)
        home.writeDepartment.send_keys(department)
        Utils.waitUntilElementIsPresent(home.writeDepartment)

        home.webSubmit = home.getElement(webTable.submit_button)
        home.webSubmit.click()
        Utils.waitUntilElementIsPresent(home.webSubmit)

        listNewName = Utils.getAllElementsRow(self.driver, name)
        assert listNewName[0].text.lower() == name.lower()
        assert listNewName[1].text.lower() == lastname.lower()
        assert listNewName[2].text == age
        assert listNewName[3].text.lower() == email.lower()
        assert listNewName[4].text == salary
        assert listNewName[5].text.lower() == department.lower()



if __name__ == '__main__':
    unittest.main()