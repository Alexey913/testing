# Добавьте класс UserRepository для управления пользователями.
# В этот класс должен быть включен метод # addUser, который добавляет пользователя в систему,
# если он прошел аутентификацию. Покройте тестами новую функциональность.

# Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов. 
# ля этого, вам потребуется расширить класс User новым свойством, указывающим,
# обладает ли пользователь админскими правами. Протестируйте данную функцию.

from user import User

class UserRepository():
    
    def __init__(self) -> None:
        self._user_repository = []

    def add_user(self, user: User) -> None:
        if user.autification == True:
            self._user_repository.append(user)

    def unlogin(self) -> None:
        self._user_repository[:] = [user for user in self._user_repository if user.admin == True]

    @property
    def user_repository(self):
        return self._user_repository


    