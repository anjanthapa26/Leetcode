# Python solution to sort an rotated array
# nums = [4,5,6,7,0,1,2], target = 0
# [3,5,1] 5 

def rotated_array(nums,target):

    bp = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            bp = i
            break
    
    def binary_search(arr,target):
        low =0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2

            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

    print(nums[:bp+1],nums[bp+1:])
    arr1 = binary_search(nums[:bp+1],target)
    arr2 = binary_search(nums[bp+1:],target)
    print(arr1,arr2)
    if (arr1 == -1 and arr2 == -1):
        return -1
    elif arr1 > -1:
        return arr1
    else:
        return len(nums[:bp+1])-1 + arr2 + 1

print(rotated_array([3,5,1],5))