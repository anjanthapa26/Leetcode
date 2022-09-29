# Python solution for the string pairs 
from collections import Counter

def num_pairs(nums,target):
    col_ = Counter(nums)
    res = 0
    for k,v in col_.items():
        if k == target[:len(k)] and target[len(k):] in col_:
            res += col_[target[len(k):]] * col_[target[:len(k)]]
        if k == target[len(k):] and k == target[:len(k)]:
            res -= col_[target[len(k):]]
    return res
        


print(num_pairs(["777","7","77","77"],'7777'))