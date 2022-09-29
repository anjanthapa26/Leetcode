def rotated_array(nums,target):
    L, H = 0, len(nums)
    while L < H:
        M = (L+H) // 2
        print(M)
        if target < nums[0] < nums[M]: # -inf
            L = M+1
        elif target >= nums[0] > nums[M]: # +inf
            H = M
        elif nums[M] < target:
            L = M+1
        elif nums[M] > target:
            H = M
        else:
            return M
        print(L,H)
    return -1

print(rotated_array([4,5,6,7,0,1,2],0))