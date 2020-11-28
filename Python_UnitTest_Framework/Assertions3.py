"""
--> assertIsNone:
assertIsNone method verifies whether give values or expression results in None pr not, if the result is none
 then python unit test will pass the test case otherwise fails the test case.

--> assertIsNotNone
assertIsNotNone method verifies whether given values are not known, if the values are None then the test case
 will be failed.

"""

import unittest as ut
from selenium import webdriver as wb

class Test(ut.TestCase):

    def test_Name1(self):
        driver=wb.Chrome()
        driver.get("https://www.google.com")
        titleOfPage= driver.title

        self.assertIsNone(titleOfPage)  #Since titleOfPage contains some value assertIsNone will fail
        driver.close()

    def test_Name2(self):
        driver = wb.Chrome()
        driver.get("https://www.google.com")
        titleOfPage = driver.title

        self.assertIsNotNone(titleOfPage)  # Since titleOfPage contains some value assertIsNotNone will pass
        driver.close()

if __name__ == "__main__":
    ut.main()
