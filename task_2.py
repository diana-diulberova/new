# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента, а значение —
# имя аргумента. Если ключ не хешируем, используйте его строковое представление

import typing


def function(**kwargs):
    my_dictionary = {}
    for key, value in kwargs.items():
        if not isinstance(value, typing.Hashable):
            my_dictionary[str(value)] = key
        else:
            my_dictionary[value] = key
    return my_dictionary


print(function(x=7, y=[1, 2, 3, 4]))
