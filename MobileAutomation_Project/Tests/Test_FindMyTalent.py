from appium import webdriver
import unittest
from selenium.webdriver.common import desired_capabilities
from Pages.MainScreen import FindMyTalent
import time


class TestFindMyTalent(unittest.TestCase):

    def setUp(self):

        desired_capab = {
            "platformName": "Android",
            "platformVersion": 8,
            "deviceName": "emulator-5554",
            "appPackage": "com.promytheus.findmytalent",
            "appActivity": "com.promytheus.findmytalent.SplashActivity",
            "appWaitActivity": "com.promytheus.findmytalent.MainActivity",
            "app": "C:\\Users\\priya\\QA\\MobileAutomation_Project\\findmytalent-prodapp-release.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capab)
        time.sleep(3)
        desired_capab["appActivity"] = "com.promytheus.findmytalent.MainActivity"

    def test_loves_running_jumping(self):
        trait_1 = FindMyTalent(self.driver)
        trait_1.select_loves_running_jumping()
        trait_1.select_playing_in_a_team()
        trait_1.select_practice_for_hours()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
