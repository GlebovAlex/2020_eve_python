# 1.What is the difference between getWindowhandles() and getwindowhandle() ?
'''
driver.getWindowHandle() is used to handle single window i.e. main window 
and driver.getWindowHandles() is used to handle multiple windows.

driver.getWindowHandle() return type is string 
and driver.getWindowHandles() return type is Set<string>.
'''
# 2.Explain how you can switch back from a frame?
'''
use switchTo()
'''
# 3.Mention what is desired capability? How is it useful in terms of Selenium?
'''
The desired capability is a series of key/value pairs that stores the browser properties like browsername,
 browser version, the path of the browser driver in the system, etc.
 to determine the behaviour of the browser at run time
 
 In mobile application automation, where the browser properties and the device properties can be set.
In Selenium grid when we want to run the test cases on a different browser with different operating systems and versions.
'''

# 4.How can you find if an element non displayed on the screen?
'''
 Element.getBoundingClientRect()
'''