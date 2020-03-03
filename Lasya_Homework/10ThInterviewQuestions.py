# What is Selenium and what is composed of?
'''
Selenium is a suite of tools for automated web testing. It is composed of

Selenium IDE (Integrated Development Environment): It is a tool for recording and playing back. 
It is a chrome and Firefox plugin
WebDriver and RC: It provides the APIs for a variety of languages like Java, .NET, PHP, etc. 
With most of the browsers Webdriver and RC works.
Grid: With the help of Grid you can distribute tests on multiple machines 
so that test can be run parallel which helps in cutting down the time required for running in-browser test suites
'''
# How will you find an element using Selenium?
'''
ID's are unique for each element so it is a common way to locate elements using ID Locator.
 It is the most common fastest and safest way to detect an element.
 Not every element has ID. Xpath can be used instead.
'''

# Explain what is assertion in Selenium and what are the types of assertion?
'''
Assertions verify that the state of the application is same to what we are expecting. 
Selenium Assertions can be of three types: “assert”, “verify”, and ” waitFor”. 
When an “assert” fails, the test is aborted. When a “verify” fails, the test will continue execution, logging the failure.
A “waitFor” command waits for some condition to become true. 
They will fail and halt the test if the condition does not become true within the current timeout setting. 
Perhaps, they will succeed immediately if the condition is already true.
'''
# Explain the difference between single and double slash in X-path?
'''
Single slash " / " : Single slash is used to create xpath with absolute  path
i. e the xpath would be created to start selection from the document node/start node.

Double slash " //  " :  Double slash is used to create xpath with relative path 
i. e the xpath would be created to start selection from anywhere wwithin the document.
'''