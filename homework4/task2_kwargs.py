def get_dict(**kwargs):
    result = {}
    for key, val in kwargs.items():
        if globals().get(key).__hash__ is None:
            result[f'{val}'] = key
        else:
            result[hash(key)] = val
    return result



name = 'Alex'
secondname = 'Terg'
bday = '09.03.1992'
d = {'a': 3}

new_dict = get_dict(name=name, secondname=secondname, bday=bday, d=d)
print(new_dict)