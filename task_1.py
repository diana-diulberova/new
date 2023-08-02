# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json

from task_from_13 import Project
from task_2_from_13 import User
import pytest


@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.json'
    yield f_name
    f_name.unlink()


@pytest.fixture
def set_json(get_file):
    my_dict = {
        "1": {
            "111": "John",
            "753": "Lily"
        },
        "2": {
            "123": "Jack"
        },
        "3": {
            "456": "Kate"
        },
        "4": {
            "789": "Sara"
        },
        "5": {
            "852": "Peter"
        },
        "6": {
            "420": "Linda"
        },
        "7": {
            "357": "Michel"
        }
    }
    with open(get_file, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f)
    project = Project.from_json_file(get_file)
    return project


def test_enter_user(set_json):
    set_json.enter(name='Linda', id_='420')
    assert set_json.admin == User('420', 'Linda')
    return set_json


def test_add_user(set_json):
    set_json.enter(name='Linda', id_='420')
    set_json.add_user('Philip', '789', '7')
    check = False
    for item in set_json.users:
        if User('789', 'Philip') == item:
            check = True
    assert check == True


def test_delete_user(set_json):
    set_json.remove_user('420')
    check = False
    for item in set_json.users:
        if User('420', 'Linda') == item:
            check = True
    assert check == False


def test_print_user(set_json):
    assert set_json.__str__() == '1 111 John\n1 753 Lily\n2 123 Jack\n3 456 Kate\n4 789 Sara' \
                                 '\n5 852 Peter\n6 420 Linda\n7 357 Michel\n'


if __name__ == '__main__':
    pytest.main(['-v'])
