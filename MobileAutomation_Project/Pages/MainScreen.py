from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import Locators
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FindMyTalent:

    def __init__(self, driver):
        self.driver = driver
        # Choice 2: Loves Running/ Jumping in screen 1
        self.loves_Running_Jumping = Locators.page1_Qtn2_xpath
        # click Next button in screen 1
        self.Next_Screen1 = Locators.page1_Next_xpath
        # Choice 2: Do They Love Playing in a Team? in screen 2
        self.playing_Team = Locators.page2_Qtn2_xpath
        # click Next button in screen 2
        self.Next_Screen2 = Locators.page2_Next_xpath
        # Choice 1: Do they like to practice a particular sport for hours? in screen 3
        self.practice_for_hours = Locators.page3_Qtn1_xpath
        # click Next button in screen 3
        self.Next_Screen3 = Locators.page3_Next_xpath

    def select_loves_running_jumping(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.loves_Running_Jumping).click()
        time.sleep(2)
        scroll = TouchAction(self.driver)
        scroll.press(x=485, y=1731).move_to(x=485, y=337).release().perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Next_Screen1).click()

    def select_playing_in_a_team(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.playing_Team).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.Next_Screen2).click()

    def select_practice_for_hours(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.practice_for_hours).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.Next_Screen3).click()
