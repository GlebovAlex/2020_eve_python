from Locators.locators import Locators
import time

class otherTabs():
    def __init__(self, driver):
        self.driver = driver

        self.stry_nextbtn_xpath = Locators.stry_nextbtn_xpath
        self.evidence_tab_next_btn = Locators.evidence_tab_next_btn
        self.training_button_next_xpath = Locators.training_button_next_xpath
        self.social_button_next_xpath = Locators.social_button_next_xpath
        self.finish_button_xpath = Locators.finish_button_xpath

    def finishOtherTabs(self):
        self.driver.find_element_by_xpath(self.stry_nextbtn_xpath).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.evidence_tab_next_btn).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.training_button_next_xpath).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.social_button_next_xpath).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.finish_button_xpath).click()
        self.driver.implicitly_wait(6)