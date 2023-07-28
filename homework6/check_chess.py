from random import randint as rnd

__all__ = ['get_pos', 'get4random_pos']

LEN = 8 # Длинна списка с координатами ферзей
CNT = 4 # Количество успешных расстановок


def get_pos(pos: list) -> tuple[list[int]]:
    pos_x, pos_y = list(i for i in pos[::2]), list(i for i in pos[1::2])
    for i in range(len(pos_x)):
        for j in range(i + 1, len(pos_x)):
            if pos_x[i] == pos_x[j] or pos_y[i] == pos_y[j] or \
                abs(pos_x[i] - pos_x[j]) == abs(pos_y[i] - pos_y[j]):
                return False
    return True

def get4random_pos(cnt: int = CNT):
    while cnt > 0:
        pos = [rnd(1, 8) for _ in range(LEN)]
        if get_pos(pos):
            yield pos
            cnt -= 1
        
        

if __name__ == '__main__':
    pos = list(map(int, input('Enter nums\n').split()))
    print(get_pos(pos))
    print(tuple(get4random_pos()))
        
    
