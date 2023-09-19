# Добавьте класс UserRepository для управления пользователями.
# В этот класс должен быть включен метод # addUser, который добавляет пользователя в систему,
# если он прошел аутентификацию. Покройте тестами новую функциональность.

from user import User

class UserRepository():
    
    def __init__(self) -> None:
        self._user_repository = []

    def add_user(self, user: User) -> None:
        if user.autification == True:
            self._user_repository.append(user)

    @property
    def user_repository(self):
        return self._user_repository
    
if __name__ == "__main__":
    m = User('al', 'al')
    