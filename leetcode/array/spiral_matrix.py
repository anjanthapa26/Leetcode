# Python solution to get the matrix in spiral order
#  matrix = [[1,2,3],[4,5,6],[7,8,9]]

def spiral_matrix(matrix):

    left,right = 0,len(matrix[0])
    top,bottom = 0,len(matrix)
    opt = []
    while (left < right) or (top < bottom):

        for i in range(left,right):
            opt.append(matrix[left][i])
            print('left->right',matrix[left][i])
        top +=1

        for i in range(top,bottom):
            opt.append(matrix[i][right-1])
            print('top-bottom',matrix[i][right-1])
        right -=1

        if not (left < right and top < bottom):
            break

        for i in range(right-1,left-1,-1):
            opt.append(matrix[bottom-1][i])
            print('right-left',matrix[bottom-1][i])
        bottom -=1

        for i in range(bottom-1,top-1,-1):
            print(left,i)
            opt.append(matrix[i][left])
            print('bottom-top',matrix[i][left])
        left +=1

    return opt

print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

