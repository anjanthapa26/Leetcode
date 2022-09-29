# Python solution to find the duplicate number
#  nums = [1,3,4,2,2]

def finding_duplicate(nums):

    slow,fast = 0,0
    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow1 = 0
    while True:
        slow = nums[slow]
        slow1 = nums[slow1]
        if slow1 == slow:
            return slow

print(finding_duplicate([1,3,4,2,2]))