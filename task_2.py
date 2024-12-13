# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

__all__ = ['my_func']


import csv
import pickle


def my_func(file_csv):
    with open(file_csv, 'r', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        all_data = []
        keys = []
        for i, item in enumerate(csv_read):
            my_dict = {}
            if i == 0:
                keys = item
            else:
                for j, elem in enumerate(item):
                    my_dict[keys[j]] = elem
            if len(my_dict) != 0:
                all_data.append(my_dict)
        res = pickle.dumps(all_data, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


if __name__ == '__main__':
    my_func('users_tab.csv')
