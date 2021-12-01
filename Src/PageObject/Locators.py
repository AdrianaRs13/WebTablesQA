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
    input_name = "#firstName"
    input_lastname = "#lastName"
    input_email = "#userEmail"
    input_age = "#age"
    input_salary = "#salary"
    input_department = "#department"
    submit_button = "//button[@id='submit']"
    add_button = "#addNewRecordButton"



class textBox(object):
    full_name = "#userName"
    email = "#userEmail"
    current_address = "#currentAddress"
    permanent_address = "#permanentAddress"
    submit_button = "#submit"
    v_full_name = "//p[@id='name']"
    v_email = "//p[@id='email']"
    v_current_address = "//p[@id='currentAddress']"
    v_permanent_address = "//p[@id='permanentAddress']"

class ModalsSM(object):
    modal = "//div[@class='modal-content']"
    button_small = "#showSmallModal"
    button_large = "#showLargeModal"
    buttonC_small = "#closeSmallModal"
    buttonC_large = "#closeLargeModal"

