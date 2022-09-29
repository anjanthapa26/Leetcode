# Python solution to rotate a matrix
#  matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def rotate_matrix(matrix):

    left,right = 0,len(matrix)-1

    while left < right:

        for i in range(right-left):

            top,bottom = left,right

            topleft = matrix[top][left+i]

            matrix[top][left+i] = matrix[bottom-i][left]

            matrix[bottom-i][left] = matrix[bottom][right-i]

            matrix[bottom][right-i] = matrix[left+i][right]

            matrix[left+i][right] = topleft

        left +=1
        right -=1
    return matrix

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))

