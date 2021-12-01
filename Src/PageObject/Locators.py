class Locator(object):
    # Google Search Page
    search_text = "//input[@name='q']"
    submit = "//input[@name='btnK']"
    # //input[@name='Google Search']"
    logo = "img.lnXdpd"

class webTable(object):
    search_text = "//input[@id = 'searchBox']"
    cierra_name = "//div[contains(text(),'Cierra')]"
    edit_button = "#edit-record-1"
    modal = "//div[@role='dialog']"
    input_name = "//input[@id='firstName']"
    submit_button = "//button[@id='submit']"

class textBox(object):
    full_name = "#userName"
    email = "#userEmail"
    current_address = "#currentAddress"
    permanent_address = "#permanentAddress"

