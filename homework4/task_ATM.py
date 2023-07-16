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
from random import randint

ACTIONS = '''
Выбирите действие:\n \
1 - Пополнить баланс\n \
2 - Снять наличные\n \
3 - Узнать остаток средств\n \
0 - Выход\n'''

TAKE_OF_CONDITION = '\nПроцент за снятие — 1.5% от суммы снятия,\
но не менее 30 и не более 600 у.е.\n\
Сумма для снятия должна быть кратна 50\n'

REPLENISH_BALANCE = '\nСумма для пополнения должны быть кратна 50.\n\
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной\n'

BALANCE = '\nБаланс:\n{}'

INPUT_ERROR = '\nError: Некорректный ввод\n'

MIN_COMMISSION = 30
MAX_COMMISSION = 600
COMMISSION = 0.015
BALANCE_LIMIT = 5_000_000
WELTH_TAX = 0.1
MIN_MONEY = 50
THIRD_OPERATION_PERCENT = 0.03
OPERATION_CNT = 3


# Функция списания средств
# Переменная tax содержит в себе расчитанный налог на богатство от введенной суммы
def take_of_money(money: int, balance: int, tax: int) -> int:
    if iscorrect_money(money) and balance >= money:
        if MIN_COMMISSION > money * COMMISSION:
            balance -= (money + MIN_COMMISSION)
        elif MAX_COMMISSION < money * COMMISSION:
            balance -= (money + MAX_COMMISSION)
        else:
            balance -= (money + (int(money * COMMISSION)))
        globals()['operations_lst'] = globals().get('operations_lst') + \
            [-(globals().get('balance') - balance + tax)]
    return balance - tax

# Функция генерирует стартовый баланс,
def get_balance() -> int:
    return randint(0, 999999)

# Функция пополнения баланса
def replenish_balance(money: int, balance: int, tax: int) -> int:
    if iscorrect_money(money):
        balance += money
        # помещаю все операции с у.е. в лист, не знаю на сколько правильный это подход
        # Не отказался бы от комментариев)
        globals()['operations_lst'] = globals().get(
            'operations_lst') + [money - tax]
    return balance - tax

# Функция проверяет кратность введенной суммы
def iscorrect_money(money: int) -> bool:
    return money % MIN_MONEY == 0

# Функция возвращает налог на богатсво от введенной суммы
def get_tax_welth(balance: int, money: int) -> int:
    return int(money * WELTH_TAX) if balance > BALANCE_LIMIT else 0


cnt: str = OPERATION_CNT  # Счетчик операций
# лист с данными об операциях с у.е.. С процентами и налогом
operations_lst: list[int] = []
balance: int = get_balance()
while True:
    print(ACTIONS)
    match input():
        case '1':
            print(BALANCE.format(balance))
            money: int = int(input(REPLENISH_BALANCE))
            # Переменная tax содержит в себе расчитанный налог на богатство от введенной суммы
            tax: int = get_tax_welth(balance, money)
            new_balance: int = replenish_balance(money, balance, tax)
            if new_balance != balance and iscorrect_money(money):
                balance = new_balance
                cnt -= 1
            else:
                balance -= tax
                print(INPUT_ERROR)
            print(BALANCE.format(balance))
        case '2':
            print(BALANCE.format(balance))
            money: int = int(input(TAKE_OF_CONDITION))
            tax: int = get_tax_welth(balance, money)
            new_balance: int = take_of_money(money, balance, tax)
            if new_balance != balance and iscorrect_money(money):
                balance = new_balance
                cnt -= 1
            else:
                balance -= tax
                print(INPUT_ERROR)
            print(BALANCE.format(balance))
        case '3':
            print(BALANCE.format(balance))
        case '0':
            print(BALANCE.format(balance))
            break
        case _:
            print(INPUT_ERROR)

    if cnt == 0:
        balance: int = balance + int(balance * THIRD_OPERATION_PERCENT)
        cnt: int = OPERATION_CNT
        print(f'Начислен процент:{BALANCE.format(balance)}')
    print(operations_lst)

print(operations_lst)
