# Разработайте класс User с методом аутентификации по логину и паролю. Метод должен возвращать true, если
# введенные логин и пароль корректны, иначе false. Протестируйте все методы

# Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов. 
# ля этого, вам потребуется расширить класс User новым свойством, указывающим,
# обладает ли пользователь админскими правами. Протестируйте данную функцию.

class User():

    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._autification = False
        self._admin_rigths = False

    def autificate(self, login: str, password: str) -> bool:
        if self._login == login and self._password == password:
            self._autification = True
        return self._autification
    
    def admin_in(self, password: str) -> bool:
        if self._password == password and self._autification:
            self._admin_rigths = True
        return self._admin_rigths
    
    def __repr__(self) -> str:
        return f'{self._login}'
    
    @property
    def login(self):
        return self._login
    
    @property
    def password(self):
        return self._password
    
    @property
    def autification(self):
        return self._autification
    
    @property
    def admin(self):
        return self._admin_rigths