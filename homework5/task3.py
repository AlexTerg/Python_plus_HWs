#Создайте функцию генератор чисел Фибоначчи

def get_fibonacci(end: int):
    a, b = 0, 1
    while end >= 0:
        yield a
        a, b = b, a + b
        end -= 1

print(*get_fibonacci(10))