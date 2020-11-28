"""
--> assertIN:
It verifies whether the first element is present in the second element, if first element is present in second element
then the test is passed otherwise test is failed.

--> assertNotIn:
it verifies whether the first element is not present in the second element or not, if first element is not present
in second element then the test is passed otherwise test is failed.

These two methods will be helpful when you want to verify the presence of a value in a list, tuple, set and
dictionary.

"""

import unittest as ut
from selenium import webdriver as wb

class Test(ut.TestCase):

    def test_Name1(self):
        li= ['python', 'java', 'selenium']

        self.assertIn('python', li)  # 1st element is need to be find in the 2nd element if found result is true

    def test_Name2(self):
        li = ['python', 'java', 'selenium']

        self.assertNotIn('C++', li)  # checks 1st element is present in the 2nd element, if not found result is true

if __name__ == "__main__":
    ut.main()
