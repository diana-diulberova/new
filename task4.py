# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>

__all__ = ['rename_func']

import os


def rename_func(new_name: str, old_extension: str, new_extension: str, dir_name: str):
    dir_list = os.listdir(dir_name)
    for i, item in enumerate(dir_list, 1):
        file_extension = item.split('.')[1]
        if file_extension == old_extension:
            file_name = os.path.join(dir_name, f'{item.split(".")[0]}_{new_name}_{i}.{new_extension}')
            old_name = os.path.join(dir_name, item)
            os.rename(old_name, file_name)


if __name__ == '__main__':
    rename_func('test', 'bin', 'txt', r'C:\Users\Пользователь\Documents\IT\Geek Brains\HW_Python_GB\Doc')
