# Доработаем задачи 3 и 4.
# Создайте класс Project, содержащий атрибуты – список
# пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя
# и проверяет есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается
# исключение доступа. Если пользователь присутствует в списке пользователей проекта, то пользователь,
# который входит получает его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем ваш
# уровень, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
import json
from task_2_from_13 import User
from task_3_from_13 import ExceptionLevel, ExceptionAccess


class Project:
    file_name = 'users.json'

    def __init__(self, users: list[User]):
        self.users = users
        self.admin: User = None

    @classmethod
    def from_json_file(cls, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            dct = json.load(f)
        my_list = []
        for access, item in dct.items():
            for id_, name in item.items():
                my_list.append(User(id_, name, access))
        return Project(my_list)

    def enter(self, name, id_):
        user_1 = User(id_, name)
        for user in self.users:
            if user_1 == user:
                self.admin = user
                break
        else:
            raise ExceptionAccess(name, id_)

    def add_user(self, name, id_, access):
        if self.admin.access > access:
            raise ExceptionLevel(name, id_, access)
        self.users.append(User(id_, name, access))

    def remove_user(self, id_):
        for user in self.users:
            if user.id_ == id_:
                self.users.remove(user)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        my_dict = {str(i): {} for i in range(1, 7 + 1)}
        for user in self.users:
            my_dict[user.access] = {str(user.id_): str(user.name)}
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def __str__(self):
        text = ''
        for item in self.users:
            text += f'{item.access} {item.id_} {item.name}\n'
        return text


if __name__ == '__main__':
    project = Project.from_json_file('file_1.json')
    print(project)
    # project.enter(name='Linda', id_='42')
    project.enter(name='Linda', id_='420')
    # project.add_user('Philip', '789', '4')
    project.add_user('Philip', '789', '7')
    print(project)
