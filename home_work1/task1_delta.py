# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = 10
b = 6
c = 5

IS_DELTA_FALSE = f'Треугольника со сторонами a = {a}, b = {b}, c = {c} не существует'
IS_ISOSCELES = 'Треугольник равнобедренный'
IS_EQUILATERAL = 'Треугольник равносторонний'
IS_SCALENE = 'Треугольник разносторонний'


def is_not_delta(a, b, c):
    return a + b < c or a + c < b or b + c < a


def is_equilateral(a, b, c):
    return a == b == c


def is_isosceles(a, b, c):
    return a == b or a == c or b == c


if is_not_delta(a, b, c):
    print(IS_DELTA_FALSE)
elif is_equilateral(a, b, c):
    print(IS_EQUILATERAL)
elif is_isosceles(a, b, c):
    print(IS_ISOSCELES)
else:
    print(IS_SCALENE)
