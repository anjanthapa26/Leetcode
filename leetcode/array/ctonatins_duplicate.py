# Python program to solve duplicate contains
#  nums = [1,2,3,1], k = 3


def contains_dup(nums,k):
    d = {}
    for i,j in enumerate(nums):
        if j in d and abs(i - d[j]) <= k:
                return True
        d[j] = i
    return False


print(contains_dup([1,2,3,1,2,3],2))