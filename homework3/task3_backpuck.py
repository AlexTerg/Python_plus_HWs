MAX_WEIGTH: int = 3000

things: dict = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
                'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
                'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}



sort_things = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))

# Функция вернет лист кортежей с ключами и значениями
def get_thingslst(data: dict) -> list:
    data_lst: list = []
    for key, val in data.items():
        data_lst.append((key, val))
    return data_lst

# Функция вернет словарь с вариантами упаковки рюкзака


def get_buckpuck(things: dict) -> dict:

    # Создал этот список для того что бы в дальнейшем мог обратиться к нужному ключу и в итоге выйти из цикла
    things_lst: list = get_thingslst(things)

    max_weigth: int = MAX_WEIGTH

    backpuck: dict = {}  # Рюкзак
    cnt_key: int = 1
    
    cnt = len(things_lst) * 5

    while len(things_lst) != 0:

        # Временный массив со значениями, которые будут падать сюда из цикла for
        temp_backpuck: list = []

        for key, val in things.items():
            if val <= max_weigth:
                max_weigth -= val
                temp_backpuck.append(key)

        # Проверка на вхождение временного листа в рюкзак
        if sorted(temp_backpuck) in backpuck.values():

            # Здесь я удаляю первую пару из пришедшего словаря и добавляю их в конец, затем удаляю первый кортеж из листа
            things.pop(things_lst[0][0])
            things[things_lst[0][0]] = things_lst[0][1]
            things_lst.pop(0)

        else:
            backpuck[cnt_key] = sorted(temp_backpuck)
            cnt_key += 1

        max_weigth: int = MAX_WEIGTH

    return backpuck


result: dict = get_buckpuck(sort_things)
for key, val in result.items():
    print(key, val)
