# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(message)s')

def collect_directory_info(dir_path):
    if not os.path.exists(dir_path):
        raise ValueError(f'Directory does not exist: {dir_path}')

    with os.scandir(dir_path) as entries:
        for entry in entries:
            file_name = os.path.splitext(entry.name)[0]
            file_extension = os.path.splitext(entry.name)[1][1:] if entry.is_file() else ''
            is_directory = entry.is_dir()
            parent_directory = os.path.basename(dir_path)

            file_info = FileInfo(name=file_name, extension=file_extension, is_dir=is_directory, parent=parent_directory)
            logging.info(file_info)

            if is_directory:
                collect_directory_info(entry.path)

if __name__ == '__main__':
    directory_path = r'C:\Users\Пользователь\Documents\IT\Geek Brains\HW_Python_GB'

    try:
        collect_directory_info(directory_path)
    except ValueError as e:
        print(e)
