import HTMLTestRunner
import unittest
from selenium import webdriver
from Pages.newTalentPage import NewTalentPage
from Pages.loginpage import LoginPage
from Pages.storyPage import storyPage
from Pages.otherTabs import otherTabs
from Pages.evidencePage import evidencePage
from Pages.trainingPage import trainingPage
from Pages.socialBackgroundPage import socialPage
import time


class TestPromytheus_AddNewTalent(unittest.TestCase):

    def setUp(cls):
        # Create a new Chrome session
        cls.driver = webdriver.Chrome(executable_path= 'C:/Users/lasya/PycharmProjects/Promethyus/chromedriver.exe')
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

        # calling other storyPage() class from storyPage file
        storyPageObj = storyPage(driver)
        storyPageObj.setStoryPage()

        # calling other evidencePage() class from evidencePage file
        evidencePageObj = evidencePage(driver)
        evidencePageObj.setevidencePage()

        # calling other trainingPage() class from trainingPage file
        trainingPageObj = trainingPage(driver)
        trainingPageObj.setTrainingPage()

        # calling other socialPage() class from socialPage file
        socialPageObj = socialPage(driver)
        socialPageObj.setSocialPage()

    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="C:/Users/lasya/PycharmProjects/Promethyus/Reports"))