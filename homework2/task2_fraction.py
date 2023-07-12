import math
import fractions


def parse_fraction_number() -> tuple[int, int]:
    numirator, denomerator = input(
        'Enter fraction value.\nExample: 2/3\n').split('/')
    return int(numirator), int(denomerator)


def get_lcm(num1: int, num2: int) -> int:
    return num1 * num2 // math.gcd(num1, num2)


def get_sum(fraction1: tuple, fraction2: tuple) -> tuple or int:

    num1, denom1 = fraction1
    num2, denom2 = fraction2

    lcm: int = get_lcm(denom1, denom2)
    lcm_num: int = get_lcm(num1, num2)

    new_num1: int = int(lcm / denom1 * num1)
    new_num2: int = int(lcm / denom2 * num2)
    
    # print(fractions.Fraction((new_num1 + new_num2) // lcm_num, lcm // lcm_num))

    if ((new_num1 + new_num2) // lcm_num) % (lcm // lcm_num) != 0:
        return f'{(new_num1 + new_num2) // lcm_num}/{lcm // lcm_num}'
    else:
        return str(((new_num1 + new_num2) // lcm_num) // (lcm // lcm_num))
    


def get_prod(fraction1: tuple, fraction2: tuple) -> tuple or int:

    num1, denom1 = fraction1
    num2, denom2 = fraction2

    lcm = get_lcm(denom1, denom2)
    lcm_num = get_lcm(num1, num2)

    new_num1: int = int(lcm / denom1 * num1)
    new_num2: int = int(lcm / denom2 * num2)
    
    # print(fractions.Fraction((new_num1 * new_num2) // lcm_num, lcm // lcm_num))

    if ((new_num1 * new_num2) // lcm_num) % (lcm // lcm_num) != 0:
        return f'{(new_num1 * new_num2) // lcm_num}/{lcm // lcm_num}'
    else:
        return str(((new_num1 * new_num2) // lcm_num) // (lcm // lcm_num))


first_fraction: tuple = parse_fraction_number()
second_fraction: tuple = parse_fraction_number()
sum_fr = get_sum(first_fraction, second_fraction)
prod_fr = get_prod(first_fraction, second_fraction)

print(f'sum of fraction = {sum_fr} and product of fraction = {prod_fr}')



# if first_value_denomerator > second_value_denomerator:
