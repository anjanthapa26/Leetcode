# Python solution to find the peak element

def peak_element(arr):
    low = 0
    high = len(arr)-1
    while low <=high:

        mid = (low + high) //2

        if mid > 0 and mid < len(arr)-1:

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid 

            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                low = mid + 1
            else:
                high = mid - 1

        elif mid == 0:
            if arr[mid] > arr[mid+1]:
                return 0
            else:
                return 1
        elif mid == len(arr)-1:
            if arr[mid-1] < arr[mid]:
                return mid
            else:
                return mid-1


print(peak_element([1,2]))