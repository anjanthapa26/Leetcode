# Python solution to find the longest consecutive secquence
# nums = [100,4,200,1,3,2]

import sys 
def longest_consecutive(nums):

    d = {}
    max_ = -sys.maxsize
    for val in nums:
        d[val] = 1
        if val+1 in d and val-1 in d:
            d[val] += (d[val+1] + d[val-1])
            d[val+1] += d[val]
        elif val-1 in d:
            d[val] += d[val-1]
        elif val+1 in d:
            d[val] += d[val+1]
            d[val+1] += d[val]
    print(d)
    return max(d, key= lambda x: d[x])

print(longest_consecutive([100,4,200,1,3,2]))