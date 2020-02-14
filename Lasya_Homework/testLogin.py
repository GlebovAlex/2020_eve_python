'''
Create Unit test program to check user Login (for example email login)
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# create a new Chrome session
driver = webdriver.Chrome(executable_path= 'C:/Users/lasya/PycharmProjects/untitled/chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()
# Navigate to the application home page
driver.get("https://accounts.google.com/ServiceLogin")
# get the search textbox
login_field = driver.find_element_by_xpath("//input[@id='identifierId']")

# enter email and password and submit
login_field.send_keys("lasyanalini99@gmail.com")
next_element = driver.find_element_by_xpath("//span[@class='RveJvd snByac']")
next_element.click()
pwd_field = driver.find_element_by_xpath("//input[@name='password']")
pwd_field.send_keys("pythonTest@9")
next_element = driver.find_element_by_xpath("//div[@id='passwordNext']//span[@class='CwaK9']")
next_element.click()
mailbox = driver.find_element_by_xpath("//div[@class='TN bzz aHS-bnt']//div[@class='aio UKr6le']")


# currently on result page using find_elements_by_class_name method

print("Login is verified")

# close the browser window
driver.quit()