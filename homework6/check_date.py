from sys import argv

__all__ = ['check_date']



def check_leapdate(year: int) -> bool:
    return not (year % 4 != 0 or year % 100 == 0 and year % 4 == 0)

def check_date(date: str) -> bool:
    day, mon, year = map(int, date.split('.'))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999):
        return False
    if mon in (4, 6, 9, 11) and day > 30:
        return False
    
    if mon == 2 and day > 29:
        return False
    
    if mon == 2 and check_leapdate(year) and day > 29:
        return False
    if mon == 2 and not check_leapdate(year) and day > 28:
        return False
    
    return True

if __name__ == '__main__':
    name, date = argv
    print(check_date(date))