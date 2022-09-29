#Python solution to find the duplicates in an array
# nums = [4,3,2,7,8,2,3,1]
# nums = [1,1,2]

def duplicate_array(nums):

    opt = []
    for idx,i in enumerate(nums):
        i = abs(i) - 1
        if nums[abs(i)] < 0:
            opt.append(abs(nums[idx]))
        else:
            nums[i] = -1 * nums[i]

    return opt

print(duplicate_array([4,3,2,7,8,2,3,1]))