import unittest
import pytest

from matrixException import MatrixLenException, MatrixMulException, LenOfTwoMatrixException

class Matrix:
    '''
    >>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4]])
    True
    '''

    def __init__(self, matrix) -> None:
        temp_len = len(matrix[0])
        for i in matrix:
            if len(i) != temp_len:
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
        return self.matrix == other.matrix

    def __add__(self, other):
        '''
        Сложение двух матриц
        '''
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise LenOfTwoMatrixException(self.matrix, other.matrix)

        result = [[self.matrix[j][i] + other.matrix[j][i]
                   for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        '''
        Умножение матриц
        '''
        if len(self.matrix[0]) != len(other.matrix):
            raise MatrixMulException(self.matrix, other.matrix)

        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                   for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]

        return Matrix(result)


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[2, 1], [4, 3]])

    def test_create_matrix(self):
        self.assertEqual(self.matrix1, Matrix([[1, 2], [3, 4]]))
        self.assertEqual(self.matrix2, Matrix([[2, 1], [4, 3]]))

    def test_not_equal(self):
        self.assertNotEqual(self.matrix1, self.matrix2)

    def test_sum_matrix(self):
        self.assertEqual(self.matrix1 + self.matrix2, Matrix([[3, 3], [7, 7]]))


@pytest.fixture
def newSet():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[2, 1], [4, 3]])
    return matrix1, matrix2


def test_mul_matrix(newSet):
    matrix1, matrix2 = newSet
    assert matrix1 * matrix2 == Matrix([[10, 7], [22, 15]])
    
def test_len_exception():
    with pytest.raises(MatrixLenException):
        Matrix([[1, 2], [3, 4, 5]])


if __name__ == '__main__':
    '''
    pytest вместе с unittest не работают
    '''
    import doctest
    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
    pytest.main(['-vv']) 
    # matrix1 = Matrix([[1, 2], [3, 4]])
    # matrix2 = Matrix([[2, 1], [4, 3]])
    # print(matrix1 == matrix2)
    # matrix_sum = matrix1 + matrix2
    # print(matrix_sum)
    # matrix_mul = matrix1 * matrix2
    # print(matrix_mul)
