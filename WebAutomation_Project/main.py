import unittest
import HtmlTestRunner
# import sys
# sys.path.insert(1, '/TestCases/')
from TestCases.TC_addNewTalent import TestPromytheus_AddNewTalent
from TestCases.TC_Login import TestPromytheus_Login
# from TestCases.TC_InvalidSignIn import Test_InvalidSignIn

# initialize test suite, test loader and test runner
suite = unittest.TestSuite()
loader = unittest.TestLoader()
runner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/priya/WebAutomation_Project/Reports")

# get all tests
addNewTalent = loader.loadTestsFromTestCase(TestPromytheus_AddNewTalent)
loginSignIn = loader.loadTestsFromTestCase(TestPromytheus_Login)
# invalidSignIn = loader.loadTestsFromTestCase(Test_InvalidSignIn)

# creating Test Suites
smokeTestSuite = unittest.TestSuite([addNewTalent])
# functionalTestSuite = unittest.TestSuite([loginSignIn, addNewTalent, invalidSignIn])

# running the test suite
runner.run(smokeTestSuite)
