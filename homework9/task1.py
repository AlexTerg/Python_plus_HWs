import csv
import json
import math
import random
from typing import Callable


def quadratic_deco(func: Callable) -> Callable:
    def get_quadratic_from_row():
        result_lst = []
        with open('file.csv') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                a, b, c = map(int, row)
                res = func(a, b, c)
                result_lst.append(res)
        return result_lst
    return get_quadratic_from_row


def result_to_json_deco(func: Callable) -> Callable:
    def write_json(*args):
        with open('result_file.json', 'a', encoding='utf-8') as file_json:
            res = func(*args)
            json.dump({'args': args, 'result': res}, file_json, indent=4, ensure_ascii=False)
        return res
    return write_json


@quadratic_deco
@result_to_json_deco
def qudartic(a, b, c):
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def generate_csv():
    with open('file.csv', 'w', encoding='utf-8', newline='') as file_csv:
        writer = csv.writer(file_csv, delimiter=' ')
        for _ in range(random.randint(100, 1000)):
            rnd_num_lst = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(rnd_num_lst)


if __name__ == '__main__':
    generate_csv()
    qudartic()
