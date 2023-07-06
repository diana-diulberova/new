# ✔Напишите функцию, которая заполняет файл (добавляет в конец)
# случайными парами чисел. ✔Первое число int, второе - float разделены
# вертикальной чертой. ✔Минимальное число - -1000, максимальное - +1000.
# ✔Количество строк и имя файла передаются как аргументы функции.

# Дорабатываем функции из предыдущих задач.
# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

__all__ = ['my_func']

from random import randint, uniform
import os

MIN_VALUE = -1000
MAX_VALUE = 1000


def my_func(count_rows: int, file_name: str, dir_name: str):
    file_path = os.path.join(dir_name, file_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if not os.path.exists(file_path):
        with open(file_path, 'a', encoding='utf-8') as f:
            for i in range(count_rows):
                f.write(f'{randint(MIN_VALUE, MAX_VALUE)}|{uniform(MIN_VALUE,MAX_VALUE)}\n')


if __name__ == '__main__':
    my_func(5, 'file_1.txt', 'HW_Python_GB')
