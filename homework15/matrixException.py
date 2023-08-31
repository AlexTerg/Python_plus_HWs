class MatrixLenException(Exception):

    def __init__(self, msg: str = 'Все элементы матрицы должны быть одной длинны') -> None:
        self.msg = msg
        super().__init__(self.msg)


class LenOfTwoMatrixException(Exception):
    def __init__(self, matrix1: list, matrix2: list) -> None:
        msg = f'Длинна первой матрицы - {len(matrix1)}, \
не совпадает с длинной второй матрицы - {len(matrix2)}'
        if len(matrix1[0]) != len(matrix2[0]):
            msg = f'Количество строк первой матрицы - {len(matrix1[0])} \
не совпадает с количеством строк второй матрицы - {len(matrix2[0])}'
        self.msg = msg
        super().__init__(self.msg)


class MatrixMulException(Exception):
    def __init__(self, matrix1: list, matrix2: list) -> None:
        self.msg = f'Количество строк первой матрицы - {len(matrix1[0])} \
не совпадает с количеством столбцов второй матрицы - {len(matrix2)}'
        super().__init__(self.msg)
