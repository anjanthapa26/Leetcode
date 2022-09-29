# Python solutio to find the kth smallest element
# matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8


def kth_smallest(matrix,k):
    return matrix[k//len(matrix)][k%len(matrix)-1]


print(kth_smallest([[1,5,9],[10,11,13],[12,13,15]],8))
