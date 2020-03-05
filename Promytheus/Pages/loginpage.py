from Locators.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # objects from locators
        self.email_textbox = Locators.textbox_email_xpath
        self.password_textbox = Locators.textbox_password_xpath
        self.login_button = Locators.button_login_id

    # Create class methods for each test steps
    def setSignIn(self):

        # application is very slow most of the time, hence adding sleep time almost after every action!

        time.sleep(6)
        self.driver.find_element_by_xpath(self.email_textbox).send_keys("lasyanalini9@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys("pythonTest@9")
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.element_to_be_clickable(By.ID, self.login_button)).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_button).click()
        time.sleep(3)