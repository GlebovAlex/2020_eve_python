from Locators.locators import Locators
from selenium.webdriver.common.keys import Keys


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        # objects from locators
        # self.login_link = locators.Locators.link_login
        self.login_link = "//li[@id='menu-item-963']//span[contains(@class,'menu-text')][contains(text(),'Login')]"
    # Create class methods for each test steps

    # Method to click 'Login' (under Menu) from home page
    def setLoginMenu(self):
        self.driver.find_element_by_xpath(self.login_link).click()
        self.driver.implicitly_wait(6)