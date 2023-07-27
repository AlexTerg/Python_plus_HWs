# Напишите однострочный генератор словаря,
# который принимает на вход три списка
# одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def dict_generate(name: list[str], rate: list[int], prem: list[str]) -> dict[str: float]:
    return {name: rate * float(prem[:-1]) / 100 for name, rate, prem in zip(name, rate, prem)}


name_lst: list[float] = ["Alex", "Bob", "Fisher"]
rate_lst: list[int] = [10000, 20000, 30000]
prem_lst: list[str] = ["10.25%", "10%", "20%"]

salary: dict[str: float] = dict_generate(name_lst, rate_lst, prem_lst)
print(salary)
