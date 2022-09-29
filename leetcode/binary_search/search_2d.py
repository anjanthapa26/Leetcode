# Python program to search elements in 2D matrix
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# [[1,1]] 2 


def bs_2d_matrix(matrix,target):

    m = len(matrix)-1
    n = len(matrix[0])-1

    low = 0
    high = m
    while low <= high:

        mid = (low + high) //2
        print(low,high)
        print(mid)
        if target >= matrix[mid][0] and target <= matrix[mid][n]:
            low_in = 0
            high_in = len(matrix[mid])-1
            count = 0

            while low_in <= high_in:

                mid_in = (low_in + high_in) // 2
                if matrix[mid][mid_in] == target:
                    return True
                if target > matrix[mid][mid_in]:
                    low_in = low_in + 1
                else:
                    high_in = high_in - 1
                count += 1

            return False
            
        elif target > matrix[mid][n]:
            low = mid + 1
        else:
            high = mid - 1


    return False


print(bs_2d_matrix([[1,1]],2))