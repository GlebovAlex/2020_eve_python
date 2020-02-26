import HtmlTestRunner
import unittest
from selenium import webdriver
from Pages.newTalentPage import NewTalentPage
from Pages.loginPage import LoginPage
import time


class TestPromytheus_AddNewTalent(unittest.TestCase):

    def setUp(cls):
        # Create a new Chrome session
        cls.driver = webdriver.Chrome(executable_path="C:/Users/priya/Promytheus/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_addNewTalent(self):
        driver = self.driver
        driver.get("https://app.promytheus.net/sign-in.html")
        LoginPage(driver).setSignIn()

        # calling the LoginPage() class from loginPage file
        newtalent = NewTalentPage(driver)
        newtalent.setCategory()  # calling the setCategory() method from the NewTalentPage() class
        newtalent.setPersonal()
        newtalent.setTalentTraits()
        newtalent.setPersonality()


    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/priya/Promytheus/Reports"))
