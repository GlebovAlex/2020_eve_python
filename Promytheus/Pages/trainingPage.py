from Locators.locators import Locators
import time


class trainingPage():
    def __init__(self, driver):
        self.driver = driver
        self.professionally_coached_xpath = Locators.professionally_coached_xpath
        self.coach_name_xpath = Locators.coach_name_xpath
        self.success_level_xpath = Locators.success_level_xpath
        self.training_button_next_xpath = Locators.training_button_next_xpath

    def setTrainingPage(self):
        self.driver.find_element_by_xpath(self.professionally_coached_xpath).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.coach_name_xpath).send_keys("Roger")
        self.driver.find_element_by_xpath(self.success_level_xpath).send_keys("High Level")
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.training_button_next_xpath).click()