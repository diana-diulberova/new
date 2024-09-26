# 2) Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
# в пару списков-архивов, которые также являются свойствами экземпляра.

# 3) Добавьте к задачам 1 и 2 строки документации для классов.

# 4) Доработаем класс Архив из задачи 2. Добавьте методы представления экземпляра
# для программиста и для пользователя.

# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class Archive:
    """The Archive training class."""

    my_list_number = []
    my_list_string = []

    def __init__(self, number, my_string):
        """Added number and my_string parameters. Append values in lists my_list_number and my_list_string."""
        self.number = number
        self.my_string = my_string
        Archive.my_list_number.append(number)
        Archive.my_list_string.append(my_string)

    def __str__(self):
        """Class representation for the print method."""
        return f'Экземпляр класса Archive с числом "{self.number}" и строкой "{self.my_string}"'

    def __repr__(self):
        """Class representation for the repr method."""
        return f'Archive({self.number}, {self.my_string})'


a = Archive(5, 'five')
print(f'{a.my_list_number = }, {a.my_list_string = }')
b = Archive(4, 'four')
print(f'{b.my_list_number = }, {b.my_list_string = }')
help(Archive)
print(a)
print(repr(b))
