from Locators import locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # objects from locators
        self.email_textbox = locators.Locators.textbox_email_xpath
        self.password_textbox = locators.Locators.textbox_password_xpath
        self.login_button = locators.Locators.button_login_id

    # Create class methods for each test steps
    def setSignIn(self):

        # application is very slow most of the time, hence adding sleep time almost after every action!

        time.sleep(6)
        self.driver.find_element_by_xpath(self.email_textbox).send_keys("qabootcamp20@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys("QAbootcampPWD1")
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.element_to_be_clickable(By.ID, self.login_button)).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_button).click()
        time.sleep(3)

    def invalidSignIn(self):

        # performs invalid sign in and checks if a warning message is displayed to the user

        time.sleep(6)
        self.driver.find_element_by_xpath(self.email_textbox).send_keys("qabootcamp20@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_id(self.login_button).click()
        time.sleep(3)

    def invalidEmail(self):

        # performs invalid sign in with a invalid email id value
        time.sleep(6)
        self.driver.find_element_by_xpath(self.email_textbox).send_keys("qabootcamp20")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys("QAbootcampPWD1")
        time.sleep(3)
        self.driver.find_element_by_id(self.login_button).click()
        time.sleep(3)

    def unregisteredEmail(self):

        # performs sign in using a valid email-id but not registered with Promytheus
        time.sleep(6)
        self.driver.find_element_by_xpath(self.email_textbox).send_keys("priya3010@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys("Qwerty@1230")
        time.sleep(3)
        self.driver.find_element_by_id(self.login_button).click()
        time.sleep(3)
