#Python solution to find the peak element
#  nums = [1,2,3,1]
# nums = [1,2,1,3,5,6,4]

def peak_element(nums):
    beg, end = 0, len(nums) - 1
    while beg <= end:
        mid = (beg + end)//2
        print(beg,end)
        print(mid)
        if nums[mid] < nums[mid + 1]:
            beg = mid + 1
        else:
            end = mid -1 

    return beg

print(peak_element([0,1,2,3,4,5]))