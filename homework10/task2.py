

import math


class Quadratic:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_quadratic(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
            return x1, x2
        elif discr == 0:
            x = -self.b / (2 * self.a)
            return x
        else:
            return None
        
quadratic = Quadratic(10, 55, 3)
print(quadratic.get_quadratic())
