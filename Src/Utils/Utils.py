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

    def getLenInTable(driver):
        #table path
        elements = driver.find_elements_by_xpath("//div[@class='rt-tbody']//div[@class='rt-tr-group']")
        iCount = 0
        for x in range(len(elements)):
            tempXpath = "//div[@class='rt-tbody']//div[{}]//div[1]//div[1]".format(x + 1)
            lastNameElement = driver.find_element_by_xpath(tempXpath)
            # the element has 1 space we validate if is just one space and the len is 1
            if lastNameElement.text == " " and len(lastNameElement.text) == 1:
                break
            iCount += 1
        return iCount

    def getAllElementsRow(driver, textFilter):
        # todos los xpaths de los elementos..
        dictWebElementsXpath = {
            0: "//div[1]",  # FirstName
            1: "//div[2]",  # lastName
            2: "//div[3]",  # Age
            3: "//div[4]",  # Email
            4: "//div[5]",  #Salary
            5: "//div[6]",  #Department
            6: "//div[7]//span[1]",  # Edit
            7: "//div[7]//span[2]",  # Delete
        }
        # nuestra lista de futuros elementos
        listOfallWebElements = list()
        # obtenemos la longitud de los elementos a buscar.
        lenTable = Utils.getLenInTable(driver)
        for c in range(lenTable):
            # vamos a recorrer cada uno para validar si nuetro texto filtro se encuentra
            tempXpath = "//div[@class='rt-tbody']//div[{}]//div[1]//div[1]".format(c + 1)
            lastNameElement = driver.find_element_by_xpath(tempXpath)
            # pasamos todo a lower en caso de que tu envies en minusculas o el texto no sea exacto en may o mins
            # aqui buscamos por First Name si este esta presente continuamos...
            if lastNameElement.text.lower() == textFilter.lower():
                # si lo encuentra... sabemos el index que es c
                tempRowXpath = "//div[@class='rt-tbody']//div[{}]//div[1]".format(c + 1)
                # recorremos todos los valores de el diccionario
                for tempElement in dictWebElementsXpath.values():

                    tempElementXpath = "{}{}".format(tempRowXpath, tempElement)
                    # agregamos a la lista
                    listOfallWebElements.append(driver.find_element_by_xpath(tempElementXpath))
                # salimos del ciclo
                break
        # si no encontro nada retornamos el error
        if len(listOfallWebElements) < 0:
            print("It was not possible to find the record -> {}".format(textFilter))

        # retornamos la lista de elementos...
        return listOfallWebElements



