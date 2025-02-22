def transpose(matrix):
    res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = matrix[j][i]
    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))