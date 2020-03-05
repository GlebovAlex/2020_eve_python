from Locators.locators import Locators
import time

class NewTalentPage():

    def __init__(self, driver):
        self.driver = driver

        # New Talent page objects from locators file
        self.button_new_xpath = Locators.button_new_xpath

        # Category tab
        self.dropdown_drpdwnbtn_xpath = Locators.dropdown_drpdwnbtn_xpath
        self.dropdown_category_xpath = Locators.dropdown_category_xpath
        self.button_Nextcatgry_xpath = Locators.button_Nextcatgry_xpath

        # Personal tab
        self.textbox_fName_xpath = Locators.textbox_fName_xpath
        self.textbox_lName_xpath = Locators.textbox_lName_xpath
        self.dropdown_country_xpath = Locators.dropdown_country_xpath
        self.textbox_address_xpath = Locators.textbox_address_xpath
        self.textbox_city_xpath = Locators.textbox_city_xpath
        self.textbox_state_xpath = Locators.textbox_state_xpath
        self.textbox_postal_xpath = Locators.textbox_postal_xpath
        self.button_Nextpersonal_xpath = Locators.button_Nextpersonal_xpath

        # Talent Traits tab
        self.button_qtn1_xpath = Locators.button_qtn1_xpath
        self.button_qtn2_xpath = Locators.button_qtn2_xpath
        self.button_qtn3_xpath = Locators.button_qtn3_xpath
        self.button_qtn4_xpath = Locators.button_qtn4_xpath
        self.button_qtn5_xpath = Locators.button_qtn5_xpath
        self.button_qtn6_xpath = Locators.button_qtn6_xpath
        self.button_qtn7_xpath = Locators.button_qtn7_xpath
        self.button_qtn8_xpath = Locators.button_qtn8_xpath
        self.button_qtn9_xpath = Locators.button_qtn9_xpath
        self.button_qtn10_xpath = Locators.button_qtn10_xpath
        self.button_qtn11_xpath = Locators.button_qtn11_xpath
        self.button_qtn12_xpath = Locators.button_qtn12_xpath
        self.button_qtn13_xpath = Locators.button_qtn13_xpath
        self.button_qtn14_xpath = Locators.button_qtn14_xpath
        self.button_qtn15_xpath = Locators.button_qtn15_xpath
        self.button_qtn16_xpath = Locators.button_qtn16_xpath
        self.button_qtn17_xpath = Locators.button_qtn17_xpath
        self.button_qtn18_xpath = Locators.button_qtn18_xpath
        self.button_qtn19_xpath = Locators.button_qtn19_xpath
        self.button_qtn20_xpath = Locators.button_qtn20_xpath
        self.button_qtn21_xpath = Locators.button_qtn21_xpath
        self.button_qtn22_xpath = Locators.button_qtn22_xpath
        self.button_NextTalent_xpath = Locators.button_NextTalent_xpath

        # Personality Traits tab
        self.checkbox_qtn1_xpath = Locators.checkbox_qtn1_xpath
        self.checkbox_qtn2_xpath = Locators.checkbox_qtn2_xpath
        self.button_NextPrsnlty_xpath = Locators.button_NextPrsnlty_xpath

    # Class method to perform category selection from the drop down list
    def setCategory(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_new_xpath).click()
        time.sleep(6)
        self.driver.find_element_by_xpath(self.dropdown_drpdwnbtn_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dropdown_category_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.button_Nextcatgry_xpath).click()

    # Class method to fill up the Personal details tab
    def setPersonal(self):
        self.driver.find_element_by_xpath(self.textbox_fName_xpath).send_keys("talentuser2")
        self.driver.find_element_by_xpath(self.textbox_lName_xpath).send_keys("talentlastname2")
        self.driver.find_element_by_xpath(self.dropdown_country_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.textbox_address_xpath).send_keys("1234 test drive")
        self.driver.find_element_by_xpath(self.textbox_city_xpath).send_keys("Santa Clara")
        self.driver.find_element_by_xpath(self.textbox_state_xpath).send_keys("California")
        self.driver.find_element_by_xpath(self.textbox_postal_xpath).send_keys("12345")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_Nextpersonal_xpath).click()

    # Class method to fill up the Talent Traits tab
    def setTalentTraits(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_qtn1_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn2_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_qtn3_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn4_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn5_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn6_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn7_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn8_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn9_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn10_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn11_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn12_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn13_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn14_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn15_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn16_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn17_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn18_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn19_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn20_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn21_xpath).click()
        self.driver.find_element_by_xpath(self.button_qtn22_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_NextTalent_xpath).click()

    # Class method to fill up the Personality Traits tab
    def setPersonality(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.checkbox_qtn1_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.checkbox_qtn2_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_NextPrsnlty_xpath).click()