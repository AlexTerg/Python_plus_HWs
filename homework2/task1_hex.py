"""Здравствуйте,  не стал делать проверку на корректность введенных данных, т.к. код будет всегда плюс минус одинаков.
    Мне не сложно ее сделать, """

HEX_NUM: int = 16
NUMBER_OF_HEX: str = '0123456789abcdef'


input_number = int(input('Enter number:\n'))


def get_hexnumber(number: int) -> str:
    result: str = ''
    while number > 0:
        result += NUMBER_OF_HEX[number % HEX_NUM]
        number //= HEX_NUM

    return result[::-1]

def isuequally(number: str) -> bool:
    return number == hex(input_number)[2:]

print(get_hexnumber(input_number))
print(isuequally(get_hexnumber(input_number)))
