# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = int(input('Enter number '))

LIMIT = 100000
PRIME_NUMBER = '{} простое число'
PRIME_NUMBER_FALSE = '{} не является простым'
LIMIT_OFF = 'не корректный ввод'


def is_prime(num):
    return num / num == 1 or num // 1 == num


def number_limit(num):
    return 0 < num <= LIMIT


if not number_limit(number):
    print(LIMIT_OFF)
elif is_prime(number):
    print(PRIME_NUMBER.format(number))
else:
    print(PRIME_NUMBER_FALSE.format(number))
