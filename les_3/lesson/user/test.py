import unittest

from user import User
from user_repository import UserRepository

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('login', 'password')

    def test_autification_sucsess(self):
        self.assertTrue(self.user.autificate('login', 'password'))

    def test_autification_wrong_password(self):
        self.assertFalse(self.user.autificate(self.user.login, ""))

    def test_autification_wrong_logind(self):
        self.assertFalse(self.user.autificate("", self.user.password))

    def test_autification_wrong_all_data(self):
        self.assertFalse(self.user.autificate("", ""))

class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('login', 'password')
        self.user_repository = UserRepository()
    
    def test_add_user_not_autificate(self):
        self.user_repository.add_user(self.user)
        self.assertNotIn(self.user, self.user_repository.user_repository, "Пользователь авторизован")

    def test_add_user_autificate(self):
        self.user.autificate('login', 'password')
        self.user_repository.add_user(self.user)
        self.assertIn(self.user, self.user_repository.user_repository, "Пользователь не прошел авторизацию")

if __name__ == "__main__":
    unittest.main()