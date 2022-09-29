#Python solution to find the mutiple duplicates
# nums = [4,3,2,7,8,2,3,1]


def multiple_duplicate(nums):

    for n in nums:
        nums[abs(n)-1] = -1 * abs(nums[abs(n)-1])
    opt = []
    for idx,val in enumerate(nums):
        if val > 0:
            opt.append(idx+1)
    return opt



print(multiple_duplicate([4,3,2,7,8,2,3,1]))