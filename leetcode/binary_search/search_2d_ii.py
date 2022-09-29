# Python solution to find the matrix in 2d mat
#  mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5


def search_2d_ii(matrix,target):
    right_mover = len(matrix[0]) - 1
    down_mover = 0
    while (right_mover < len(matrix[0]) and right_mover > -1 and down_mover < len(matrix)):
        if target == matrix[down_mover][right_mover]:
            return True

        if target > matrix[down_mover][right_mover]:
            down_mover +=1
        else:
            right_mover -=1
    return False

print(search_2d_ii([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],25))
