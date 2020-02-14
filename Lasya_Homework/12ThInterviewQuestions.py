# 1. Explain how you will login into any site if it is showing any authentication popup for username and password?
'''
by passing username:password along with URL "http://Username:Password@SiteURL"
'''

# 2. How do you upload a file using Selenium WebDriver?
'''
Uploading files in WebDriver is done by simply using the send_keys() method on the ‘file select’ input field 
i.e. just enter the path to the file to be uploaded.
'''

# 3.How to switch to a new window (new tab) which opens up after you click on a link?
'''
driver.execute_script("window.open('http://google.com', 'new_window')")

for switching:
driver.switch_to_window(driver.window_handles[0])
'''