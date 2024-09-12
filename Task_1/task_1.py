# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from date_validate import date_validate


if __name__ == "__main__":
    print(date_validate("54.05.2021"))
    print(date_validate("23.01.2022"))
