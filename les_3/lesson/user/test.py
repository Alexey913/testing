import unittest

from user import User

class TestMoodAnalyser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('login', 'password')

    def test_autification_sucsess(self):
        self.assertTrue(self.user.autification('login', 'password'))

    def test_autification_wrong_password(self):
        self.assertFalse(self.user.autification(self.user.login, ""))

    def test_autification_wrong_logind(self):
        self.assertFalse(self.user.autification("", self.user.password))

    def test_autification_wrong_all_data(self):
        self.assertFalse(self.user.autification("", ""))

if __name__ == "__main__":
    unittest.main()