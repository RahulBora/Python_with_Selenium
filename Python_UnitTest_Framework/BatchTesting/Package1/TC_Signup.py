import unittest as ut

class SignUpTest(ut.TestCase):
    def test_signupByEmail(self):
        print("This is signup by email text")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("This is signup by Facebook text")
        self.assertTrue(True)

    def test_signupByTwitter(self):
        print("This is signup by Twitter text")
        self.assertTrue(True)


if __name__ == "__main__":
    ut.main()