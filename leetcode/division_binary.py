#Python solution for the highest score of binary array
# nums = [0,0,1,0]
import sys
def max_score(nums):
    d = {}
    i =0
    left = nums[:i].count(0)
    right = nums[i:].count(1)
    total = left + right
    d[total] = 0
    while i < len(nums):
        left += int(nums[i] == 0)
        right -= int(nums[i]==1)
        total = left + right
        if total not in d:
            d[total] = [i+1]
        else:
            d[total].append(i+1)
        i +=1 
    return d[max(d)]


def maxScoreIndices(nums):
    left_div_score = 0
    right_div_score = sum(nums)
    
    div_sum = [left_div_score+right_div_score]
    print(div_sum)
    
    for i in range(len(nums)):
        if nums[i]==0:
            left_div_score+=1
        if nums[i]==1:
            right_div_score-=1
        div_sum.append(left_div_score+right_div_score)
            
    max_val = max(div_sum)
    
    return( [i for i, v in enumerate(div_sum) if v==max_val])

print(maxScoreIndices([0,0,1,0]))
    

