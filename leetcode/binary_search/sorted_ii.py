#Python solution to find the element in duplicate rotated sorted array
# nums = [2,5,6,0,0,1,2], target = 0
# [1,0,1,1,1] 0
# [1,3] 3 

def rotated_sorted(nums,target):
    low = 0
    high = len(nums) -1 

    while low <= high:

        mid = (low + high) //2
        while low < high and nums[low] == nums[low+1]:
            low +=1
        while low < high and nums[high] == nums[high-1]:
            high -=1

        mid = (low + high) //2
        if nums[mid] == target:
            return True
        
        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                high = mid - 1
            else:
                low = mid + 1
    return False

print(rotated_sorted([1,3],3))
