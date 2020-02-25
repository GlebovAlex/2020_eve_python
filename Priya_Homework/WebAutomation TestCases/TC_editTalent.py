import HtmlTestRunner
import unittest
from selenium import webdriver
from Pages.editTalent import EditTalent
from Pages.loginPage import LoginPage


class TestPromytheus_AddNewTalent(unittest.TestCase):

    def setUp(cls):
        # Create a new Chrome session
        cls.driver = webdriver.Chrome(executable_path="C:/Users/priya/Promytheus/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_editTalent(self):
        driver = self.driver
        driver.get("https://app.promytheus.net/sign-in.html")
        LoginPage(driver).setSignIn()
        edittalent = EditTalent(driver)
        edittalent.setEditTalent()
        edittalent.setTalentTraits()
        edittalent.setPersonality()

    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/priya/Promytheus/Reports"))