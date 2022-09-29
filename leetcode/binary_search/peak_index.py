# Python solution for the peak index array
# arr = [0,1,0]

def peak_index(arr):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if mid -1 > -1 or (mid + 1) < len(arr):
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid

        if arr[mid-1] < arr[mid]:
            low = mid
        elif arr[mid-1] > arr[mid]:
            print('entered')
            high = mid - 1

print(peak_index([0,2,1,0]))


        