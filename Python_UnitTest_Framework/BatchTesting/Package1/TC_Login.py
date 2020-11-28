import unittest as ut

class LoginTest(ut.TestCase):
    def test_loginByEmail(self):
        print("This is login by email text")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("This is login by Facebook text")
        self.assertTrue(True)

    def test_loginByTwitter(self):
        print("This is login by Twitter text")
        self.assertTrue(True)


if __name__ == "__main__":
    ut.main()