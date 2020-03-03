# How to switch to a new window (new tab) which opens up after you click on a link?
'''next_element = driver.find_element_by_xpath("//span[@class='RveJvd snByac']")
next_element.click()
'''

# How to handle a dropdown in Selenium WebDriver? How to select a value from dropdown?
'''
Import the package org.openqa.selenium.support.ui.Select
Instantiate the drop-down box as a "Select" object in WebDriver

import org.openqa.selenium.support.ui.Select
select drpcountry = new select(driver.findelement(By.name("country")))
drpcountry.selectByVisibleText("AMERICA")
'''

# How to scroll down to a particular element?
'''
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element_by_id("my-id")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

Or, you can also "scroll into view" via scrollIntoView():
'''
"""
scrollIntoView
The DOM method scrollIntoView only scrolls the element into view. If scrollIntoView cannot scroll the element into view,
it will just fail silently.
I added an invisible element to the start of body and called scrollIntoView on it. 
Nothing scrolled but there was no error.
Note that you have more control on how the element is scrolled with scrollIntoView than with moveToElement.
Selenium is only interested in bringing the element into view so that the mouse can be placed on it. 
It does not give you any say in how it is going to do it. scrollIntoView however allows you, for instance,
to specify whether you want the top or bottom of the element to be align with its scrollable ancestor. 
(See here for the details.)

moveToElement
The Selenium method moveToElement does two things: it scrolls the element into view and moves the mouse on top of the element.
I've also tested it with elements that cannot be scrolled or moved to because they have no coordinates on screen and got no error here either.
"""

# What is POM (Page Object Model)? What are its advantages?
'''
It is widely used design pattern in Selenium for enhancing test maintenance and reducing code duplication. 
Page object model (POM) can be used in any kind of framework such as modular, data-driven, keyword driven, hybrid framework etc.  
A page object is an object-oriented class that serves as an interface to a page of your Application Under Test(AUT). 
The tests then use the methods of this page object class whenever they need to interact with the User Interface (UI) of that page.
The benefit is that if the UI changes for the page, the tests themselves don’t need to change, only the code within the page object needs to change. 
Subsequently, all changes to support that new UI is located in one place.

Code reusability,Code maintainability,Object Repository,Readability
'''