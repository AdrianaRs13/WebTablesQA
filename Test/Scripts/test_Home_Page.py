import sys

sys.path.append(sys.path[0] + "/...")

from Search.Src.TestBase.WebDriverSetup import WebDriverSetup
from Search.Src.PageObject.Pages.HomePage import Home
import unittest
from selenium import webdriver
from Search.Src.Utils.Utils import Utils


class Google_HomePage(WebDriverSetup):
    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        # self.driver.set_page_load_timeout(30)
        Utils.page_is_loading(self.driver)

        web_page_title = "Google"
        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home_page = Home(driver)


if __name__ == '__main__':
    unittest.main()