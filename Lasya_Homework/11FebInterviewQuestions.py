# What are the advantages of Selenium?
'''
Open-Source,Supports languages,Supports Operating Systems,Support across browsers,
    The browsers supported by the Selenium packages are:
        Selenium IDE can be used with chrome and Firefox as a plug-in
        Selenium RC and Webdriver supports diverse browsers such as Internet Explorer

Support for programming language and framework:
    Selenium integrates with programming languages and various frameworks. 
    For instance, it can integrate with ANT or Maven type of framework for source code compilation. Further,
    it can integrate with TestNG testing framework for testing applications and reporting purposes. 
    It can integrate with Jenkins or Hudson for Continuous Integration (CI) 
    and can even integrate with other Open-Source tools to supports other features.
    
Tests across devices,Constant updates,Ease of implementation,Loaded Selenium Suits:
    Selenium is not just a singular tool or utility, it a loaded package of various testing tools and so is referred to as a Suite.
    Each tool is designed to cater to different testing needs and requirements of test environments.
    Additionally, Selenium comes with capabilities to support Selenium IDE, Selenium Grid, and Selenium Remote Control (RC).

Reusability and Add-ons:
    Selenium Test Automation Framework uses scripts that can be tested directly across multiple browsers. 
    Concurrently, it is possible to execute multiple tests with Selenium,
    as it covers almost all aspects of functional testing by implementing add-on tools that broaden the scope of testing.
'''

# What are the four parameter you have to pass in Selenium?
'''
Four parameters that you have to pass in Selenium are:
    Host
    Port Number
    Browser
    URL
'''
# What is the difference between setSpeed() and sleep()
'''
Both of these methods delay the speed of execution.
The main difference between them is setSpeed sets a speed while it  will apply delay time before every Selenium operation
takes place. thread.sleep() will set up wait only for once.

For Example:
sleep(5000)- It will wait for 5 seconds. It is executed only once, where the command is written.
setSpeed("5000")- It also will wait for 5 seconds. 
It runs each command after setSpeed delay by the number of milliseconds mentioned in set Speed.
'''
# What is same origin policy? How you can avoid same origin policy?
'''
The same-origin policy is a critical security mechanism that restricts how a document 
or script loaded from one origin can interact with a resource from another origin. 
It helps isolate potentially malicious documents, reducing possible attack vectors.

For example JavaScript from “website1.example” cannot access my profile data in “website2.example/myprofile” 
because again Same Origin Policy doesn’t allow Cross Origin reads.

JSONP,CORS
'''