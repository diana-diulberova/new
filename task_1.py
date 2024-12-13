# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

__all__ = ['my_func']


import pickle
import csv


def my_func(file_pickle, file_csv):
    with (open(file_pickle, 'rb') as f_read,
          open(file_csv, 'w', newline='', encoding='utf-8') as f_write
          ):
        new_dict = pickle.load(f_read)
        csv_write = csv.DictWriter(f_write, fieldnames=['id', 'level', 'name'],
                                   dialect='excel-tab', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(new_dict)


if __name__ == '__main__':
    my_func('user.pickle', 'users_tab.csv')
