from Locators.locators import Locators
import time

class storyPage():
    def __init__(self, driver):
        self.driver = driver


        self.story_age_xpath = Locators.story_age_xpath
        self.story_interest_level_xpath = Locators.story_interest_level_xpath
        self.stry_nextbtn_xpath = Locators.stry_nextbtn_xpath

    def setStoryPage(self):
        self.driver.find_element_by_xpath(self.story_age_xpath).send_keys("9")
        time.sleep(6)
        self.driver.find_element_by_xpath(self.stry_nextbtn_xpath).click()
        self.driver.implicitly_wait(6)