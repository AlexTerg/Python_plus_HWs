
def transportation(matrix: list) -> list:
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



for item in transportation(lst):
    print(item)
