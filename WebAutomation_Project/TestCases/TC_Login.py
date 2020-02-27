import HtmlTestRunner
import unittest
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Locators.locators import Locators
import time
import sys
sys.path.append("C:/Users/priya/Promytheus")


class TestPromytheus_Login(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Create a new Chrome session
        cls.driver = webdriver.Chrome(executable_path="C:/Users/priya/Promytheus/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_validLogin(self):
        driver = self.driver
        driver.get(Locators.url)
        # calling the HomePage() class from homePage file
        login = HomePage(driver)
        login.setLoginMenu() # calling the setLoginMenu() method from the HomePage() class
        time.sleep(6)
        print(driver.title)
        self.assertIn("Sign In", driver.title)

    def test_validSignIn(self):
        driver = self.driver
        driver.get("https://app.promytheus.net/sign-in.html")
        # calling the LoginPage() class from loginPage file
        signin = LoginPage(driver)
        signin.setSignIn() # calling the setSignIn() method from the LoginPage() class
        print(driver.title)
        self.assertIn("Talents", driver.title)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/priya/Promytheus/Reports"))
