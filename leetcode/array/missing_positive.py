#Python solution to find the missing positive number
# nums = [1,2,0]

def missing_positive(nums):
    min_ = min(nums)
    tester = 1
    i = 0
    s = set()
    if min_ > 1:
        return 1
    else:
        while i < len(nums):
            if nums[i] > 0:
                if (tester > nums[i] or tester == nums[i]) and nums[i] not in s:
                    tester +=1
                s.add(nums[i])
            i +=1
    while tester in s:
        tester +=1
    return tester


print(missing_positive([1,1]))


