"""
--> assertTrue:
when we have only two parameters we can use assertEqual method to check whether both are same or not, but if we have
more than two parameters, comparing values with assertEqual method become more difficult

assertTrue method checks whether given parameter is true or not, if value is true then test is passed otherwise
test is failed.

--> assertFalse:
assertFalse method compares whether given value or expression result is false or not.

if the result or value is False then unit test passes the testcase but if the result is true unit test fails
the test case.
"""


import unittest as ut
from selenium import webdriver as wb

class Test(ut.TestCase):

    def test_Name1(self):
        driver=wb.Chrome()
        driver.get("https://www.google.com")
        titleOfPage= driver.title

        self.assertTrue(titleOfPage == "Google")  #True
        driver.close()

    def test_Name2(self):
        driver = wb.Chrome()
        driver.get("https://www.google.com")
        titleOfPage = driver.title

        self.assertFalse(titleOfPage == "Google")  # False
        driver.close()

if __name__ == "__main__":
    ut.main()
