# python solution to find out the number of pairs of string
from collections import Counter
def numOfPairs(nums,target):
    freq = Counter(nums)
    ans = 0 
    for k, v in freq.items(): 
        if target.startswith(k): 
            suffix = target[len(k):]
            ans += v * freq[suffix]
            print(ans)
            if k == suffix: 
                ans -= freq[suffix]
    return ans 

print(numOfPairs(["777","7","77","77"],"7777"))




