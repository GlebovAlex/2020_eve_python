from Locators.locators import Locators
import time


class evidencePage():
    def __init__(self, driver):
        self.driver = driver
        self.friends_check_xpath = Locators.friends_check_xpath
        self.talent_work_product_xpath = Locators.talent_work_product_xpath
        self.evidence_tab_next_btn = Locators.evidence_tab_next_btn

    def setevidencePage(self):
        self.driver.find_element_by_xpath(self.friends_check_xpath).click()
        time.sleep(6)
        self.driver.find_element_by_xpath(self.talent_work_product_xpath).send_keys("Testing this by sending input")
        self.driver.find_element_by_xpath(self.evidence_tab_next_btn).click()
        self.driver.implicitly_wait(6)