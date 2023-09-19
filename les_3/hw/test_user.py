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

    def test_admin_user_create(self):
        self.user.autificate('login', 'password')
        self.user.admin_in('password')
        self.assertTrue(self.user.admin)

    def test_admin_user_not_autificate(self):
        self.user.admin_in('password')
        self.assertFalse(self.user.admin)
    
    def test_admin_user_wrong_pass(self):
        self.user.autificate('login', 'password')
        self.user.admin_in('pass')
        self.assertFalse(self.user.admin)

    def test_admin_user_not_autificate_wrong_pass(self):
        self.user.admin_in('pass')
        self.assertFalse(self.user.admin)

class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()
        self.user_1 = User('login', 'password')
        self.user_1.autificate('login', 'password')
        self.user_2 = User('log', 'pass')
        self.admin_1 = User('admin_1', 'pass')
        self.admin_1.autificate('admin_1', 'pass')
        self.admin_1.admin_in('pass')
        self.admin_2 = User('admin_2', 'pass')
        self.admin_2.autificate('admin_2', 'pass')
        self.admin_2.admin_in('pass')

    def test_add_user_not_autificate(self):
        self.user_repository.add_user(self.user_2)
        self.assertNotIn(self.user_1, self.user_repository.user_repository, "Пользователь авторизован")

    def test_add_user_autificate(self):
        self.user_repository.add_user(self.user_1)
        self.assertIn(self.user_1, self.user_repository.user_repository, "Пользователь не прошел авторизацию")

    def test_unlogin(self):

        self.user_2.autificate('log', 'pass')
        self.user_repository.add_user(self.user_2)
        self.user_repository.add_user(self.admin_1)
        self.user_repository.add_user(self.admin_2)
        self.user_repository.unlogin()
        self.assertNotIn(self.user_1, self.user_repository.user_repository)
        self.assertNotIn(self.user_1, self.user_repository.user_repository)
        self.assertIn(self.admin_1, self.user_repository.user_repository)
        self.assertIn(self.admin_2, self.user_repository.user_repository)

if __name__ == "__main__":
    unittest.main()