# Python solution to find the kth closest integer to x 
# arr = [1,2,3,4,5], k = 4, x = 3


def kth_closest_element(arr,k,x):

    low = 0
    high = len(arr)-1
    opt = []
    while low <= high:
        mid = (low+high) //2

        if arr[mid] == x:
            break
        
        if x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
    def value_extracter(left,right,k):
        while k > 0:
            if left == 0 and right == -1:
                while k > 0:
                    opt.append(arr[left])
                    left +=1
                    k -=1
                break
            if left == len(arr) and right == len(arr)-1:
                while k > 0:
                    opt.append(arr[right])
                    right -=1
                    k -=1
                break

            if left > -1 and right < len(arr):
                if abs(arr[left] - x) < abs(arr[right] - x) or abs(arr[left] -x) == abs(arr[right] - x) and arr[left] < arr[right]:
                    opt.append(arr[left])
                    left -=1
                else:
                    opt.append(arr[right])
                    right +=1
            else:
                if left > -1:
                    opt.append(arr[left])
                    left -=1
                if right < len(arr):
                    opt.append(arr[right])
                    right +=1
            k -=1


    if arr[mid] == x:
        opt.append(arr[mid])
        k -=1
        left,right = mid,mid
        value_extracter(left-1,right+1,k)
    else:
        value_extracter(low,high,k)

    return sorted(opt)

print(kth_closest_element([0,1,1,1,2,3,6,7,8,9],9,4))


                
                

