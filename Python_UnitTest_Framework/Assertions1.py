"""
1. Assertion is a checkpoint or we can say it's averification for the  test case to evaluate
some item on the execution.

2. If we do not provide any assertion inside a test case then there is no way to know whether a test case
is failed or not.

3. Assertion helps in report generation, based on the assertions the test execution report will be generated.

4. There are few assertion which will accept all the values and few assertions will accept only numeric value.
 """

"""
--> assertEqual:
assert Equal compare the first parameter with the second parameter, if both matches the unit test will continue
with the remaining execution but both the values are different then unit test fails the test testcase.

--> assertNotEqual:
assertNotEqual compares the given two parameters, if both parameter are not same then unit test passes the test
case but if both parameter are same then unit test fails the test case.
"""

import unittest as ut
from selenium import webdriver as wb


class Test(ut.TestCase):
    def testName1(self):
        driver= wb.Chrome()
        driver.get("https://www.google.com")
        titleOfPage=driver.title

        #assertEqual
        self.assertEqual("Google",titleOfPage, "WebPage titles are same")
        driver.close()

    def testName2(self):
        driver = wb.Chrome()
        driver.get("https://www.google.com")
        titleOfPage = driver.title

        # assertNotEqual
        self.assertNotEqual("Google123", titleOfPage, "WebPage titles are not  same")
        driver.close()


if __name__ == "__main__":
    ut.main()