import time

from Search.Src.TestBase.WebDriverSetup import WebDriverSetup


class Utils(WebDriverSetup):
    def page_is_loading(driver):
        bstatus = False
        while bstatus:
            time.sleep(3500)
            domStatus = driver.execute_script("return document.readyState")
            bstatus = "complete" in domStatus

    def waitUntilElementIsPresent(WebElement):
        status = False
        time.sleep(5)
        while status:
            WebElement.is_enabled() and WebElement.is_displayed()
            time.sleep(5)
        return

# class validateModal():
# status = javascript("document.getElementByID('')")
