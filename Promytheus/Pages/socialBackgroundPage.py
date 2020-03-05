from selenium.webdriver.support.ui import Select
from Locators.locators import Locators
import time

class socialPage():
    def __init__(self, driver):
        self.driver = driver
        self.marital_status_xpath = Locators.marital_status_xpath
        self.social_button_next_xpath = Locators.social_button_next_xpath
        self.finish_button_xpath = Locators.finish_button_xpath

    def setSocialPage(self):
        self.driver.find_element_by_xpath(self.marital_status_xpath).click()
        self.driver.implicitly_wait(6)
        select = Select(self.driver.find_element_by_xpath(self.marital_status_xpath))
        select.select_by_value('MARRIED')
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.social_button_next_xpath).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.finish_button_xpath).click()