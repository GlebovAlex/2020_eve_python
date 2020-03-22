from appium import webdriver
from Locators.locators import Locators
from appium.webdriver.common.touch_action import TouchAction

desired_capabilites = {
    "platformName": "Android",
    "platformVersion": 8,
    "deviceName": "emulator-5554",
    "appPackage": "com.promytheus.findmytalent",
    "appActivity": "com.promytheus.findmytalent.SplashActivity",
    "appWaitActivity": "com.promytheus.findmytalent.MainActivity",
    "app": "C:\\Users\\priya\\QA\\MobileAutomation_Project\\findmytalent-prodapp-release.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilites)

# choose "" option from the questions listed in find my talent page

driver.implicitly_wait(3)
driver.find_element_by_xpath(Locators.page1_Qtn2_xpath).click()
driver.implicitly_wait(3)
scroll = TouchAction(driver)
scroll.press(x=485, y=1731).move_to(x=485, y=337).release().perform()
driver.implicitly_wait(3)
driver.find_element_by_xpath(Locators.page1_Next_xpath).click()
driver.implicitly_wait(3)
driver.find_element_by_xpath(Locators.page2_Qtn2_xpath).click()
driver.implicitly_wait(3)
driver.find_element_by_xpath(Locators.page2_Next_xpath).click()
driver.implicitly_wait(3)
driver.find_element_by_xpath(Locators.page3_Qtn1_xpath).click()
driver.implicitly_wait(3)
driver.find_element_by_xpath(Locators.page3_Next_xpath).click()
driver.implicitly_wait(3)
