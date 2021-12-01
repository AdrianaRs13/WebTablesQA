import time

from Search.Src.TestBase.WebDriverSetup import WebDriverSetup


class Utils(WebDriverSetup):
    def page_is_loading(driver):
        bstatus = False
        while bstatus:
            time.sleep(3.5)
            domStatus = driver.execute_script("return document.readyState")
            bstatus = "complete" in domStatus

    def waitUntilElementIsPresent(WebElement):
        status = False
        time.sleep(4)
        while status:
            WebElement.is_enabled() and WebElement.is_displayed()
            time.sleep(4)
        return

# class validateModal():
# status = javascript("document.getElementByID('')")
