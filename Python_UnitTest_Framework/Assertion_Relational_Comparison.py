"""
--> assertGreater
Verifies whether first value is greater than second value or not

--> assertGreaterEqual
Verifies whether first value is greater or equal to the second value or not

--> assertLess
Verifies whether first value is Lesser than second value or not

--> assertLessEqual
Verifies whether first value is Lesser or equal to the second value or not

"""

import unittest as ut
from selenium import webdriver as wb

class Test(ut.TestCase):
    a=100
    b=10
    c=100

    def test_Name1(self):
        # 1st element is need to be greater than the 2nd element, if found result is true
        self.assertGreater(self.a,self.b)

    def test_Name2(self):
        # 1st element is need to be greater than or equal to the 2nd element, if found result is true
        self.assertGreaterEqual(self.a, self.c)

    def test_Name3(self):
        # 1st element is need to be lesser than the 2nd element, if found result is true
        self.assertLess(self.b, self.a)

    def test_Name4(self):
        # 1st element is need to be lesser than or equal to the 2nd element, if found result is true
        self.assertGreaterEqual(self.a, self.c)

if __name__ == "__main__":
    ut.main()


