# Python solution to replace elements in array
# Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
# [1,2]
# [[1,3],[2,1],[3,2]]

def replace_elements(nums,operations):
    d = {}
    for idx,val in enumerate(nums):
        d[val] = idx

    i = 0
    while i < len(operations):
        nums[d[operations[i][0]]] = operations[i][1]
        d[operations[i][1]] = d[operations[i][0]]
        del d[operations[i][0]]
        i+=1
    return nums

print(replace_elements([1,2],[[1,3],[2,1],[3,2]]))

