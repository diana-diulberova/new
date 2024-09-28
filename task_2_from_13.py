# Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей

class User:
    def __init__(self, id_, name, access=None):
        self.id_ = id_
        self.name = name
        self.access = access

    def __eq__(self, other):
        return self.id_ == other.id_ and self.name == other.name

    def __str__(self):
        return f'{self.access} {self.id_} {self.name}'
