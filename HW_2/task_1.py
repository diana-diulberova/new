# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

MINIMUM_BILL = 50
PERCENT = 0.015
LOW_LIMIT = 30
UP_LIMIT = 600
THIRD_PERCENT = 0.03
WEALTH_TAX = 0.1

operation = True
balance = 0
count = 0

def is_bill():
    check = True
    cash = 0
    while check:
        cash = int(input('Введите сумму, кратную 50 у.е.: '))
        if cash % MINIMUM_BILL == 0:
            check = False
        else:
            print('Ошибка! Сумма не кратна 50 у.е.', MINIMUM_BILL)
    return cash


def deposit(balance: int):
    cash = is_bill()
    print(balance, '+', cash)
    balance += cash
    return balance


def withdrawal(balance: int):
    cash = is_bill()
    percents = 0
    if LOW_LIMIT < balance * PERCENT < UP_LIMIT:
        percents = balance * PERCENT
    elif balance * PERCENT < LOW_LIMIT:
        percents = LOW_LIMIT
    else:
        percents = UP_LIMIT
    if balance + percents >= cash:
        print(balance, '-', percents, '-', cash)
        balance -= percents + cash
    else:
        print('Ошибка! Сумма списания превышает баланс.')
    return balance


def is_reach(balance: int):
    if balance >= 5_000_000:
        print('Внимание! Налог на богатство.')
        print(balance, '-', balance * WEALTH_TAX)
        balance -= balance * WEALTH_TAX
    return balance


def menu():
    print('Для снятия наличных наберите 1')
    print('Для внесения наличных наберите 2')
    print('Для выхода наберите 3')
    return input()

while operation:
    count += 1
    balance = is_reach(balance)
    num = menu()
    if num == '1':
        balance = withdrawal(balance)
    elif num == '2':
        balance = deposit(balance)
    elif num == '3':
        operation = False
    else:
        print('Ошибка! Некорректный ввод.')
    if count % 3 == 0:
        print('Пополнение баланса на 3%')
        print(balance, '+', balance * THIRD_PERCENT)
        balance += balance * THIRD_PERCENT
    print('Текущий баланс равен', balance)