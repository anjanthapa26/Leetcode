#Python solution for zero matrix
# matrix = [[1,1,1],[1,0,1],[1,1,1]]


def zeros_matrix(matrix):

    row,col = len(matrix),len(matrix[0])
    zero_val_matrix = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_val_matrix.append((i,j))

    for i,j in zero_val_matrix:
        matrix[i] = [0] * len(matrix[0])
        for val in range(row):
            matrix[val][j] = 0


    return matrix


zeros_matrix([[1,1,1],[1,0,1],[1,1,1]])
