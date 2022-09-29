#Python solution to replace elements with greatest on right side 
# arr = [17,18,5,4,6,1]
def replace_greatest(arr):

    for i in range(len(arr)-1):
        arr[i] = max(arr[i+1:])
    arr[-1] = -1
    return arr


def replace_greatest1(arr):
    prev = arr[-1]
    arr[-1] = -1
    for i in range(len(arr)-2,-1,-1):
        holder = arr[i]
        arr[i] = max(prev,arr[i+1])
        prev = holder
    return arr
print(replace_greatest1([17,18,5,4,6,1]))