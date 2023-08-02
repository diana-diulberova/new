# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass


class ExceptionLevel(MyException):
    def __init__(self, name, id_, access):
        self.name = name
        self.id_ = id_
        self.access = access

    def __str__(self):
        return f'Ошибка! Невозможно добавить пользователя с именем {self.name} {self.id_}!\n' \
               f'Уровень доступа {self.access} выше, чем уровень доступа администратора!'


class ExceptionAccess(MyException):
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

    def __str__(self):
        return f'Ошибка доступа! Пользователя с именем {self.name} и id {self.id_} не существует.'
