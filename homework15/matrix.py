from matrixException import MatrixLenException, LenOfTwoMatrixException, MatrixMulException

import logging


class Matrix:
    
    logging.basicConfig(filename='matrix_info.log', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    

    def __init__(self, matrix) -> None:
        temp_len = len(matrix[0])
        for i in matrix:
            if len(i) != temp_len:
                self.logger.error(MatrixLenException())
                raise MatrixLenException()
        self.matrix = matrix

    def __str__(self) -> str:
        '''
        Вывод матрицы на печать
        '''
        return '\n'.join(str(i) for i in self.matrix)

    def __eq__(self, other) -> bool:
        '''
        Сравнение двух матриц
        '''
        self.logger.info(f'Сравнение матиц: {self.matrix} и {other.matrix} : {self.matrix == other.matrix}')
        return self.matrix == other.matrix

    def __add__(self, other):
        '''
        Сложение двух матриц
        '''
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            self.logger.error(LenOfTwoMatrixException(self.matrix, other.matrix))
            raise LenOfTwoMatrixException(self.matrix, other.matrix)
            

        result = [[self.matrix[j][i] + other.matrix[j][i]
                   for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
        self.logger.info(f'{self.matrix} + {other.matrix} = {result}')
        return Matrix(result)

    def __mul__(self, other):
        '''
        Умножение матриц
        '''
        if len(self.matrix[0]) != len(other.matrix):
            self.logger.error(MatrixMulException(self.matrix, other.matrix))
            raise MatrixMulException(self.matrix, other.matrix)
        
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                   for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        self.logger.info(f'{self.matrix} * {other.matrix} = {result}')
        return Matrix(result)
    


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[2, 1], [4, 3]])
    print(matrix1 == matrix2)
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)
    matrix_mul = matrix1 * matrix2
    print(matrix_mul)
