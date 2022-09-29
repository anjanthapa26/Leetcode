#python solution for last stone weight
# stones = [2,7,4,1,8,1]
import heapq

def last_stones(stones):
    for i, s in enumerate(stones):
        stones[i] = -s
    heapq.heapify(stones) 
    print(stones) # pass all negated values into the min-heap
    while stones:
        s1 = heapq.heappop(stones)  # the heaviest stone
        if not stones:  # s1 is the remaining stone
            return s1
        s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
        if s1 > s2:
            heappush(stones, s2-s1)  # push the NEGATED value of s1-s2; i.e., s2-s1
        # else s1 == s2; both stones are destroyed
    return 0  # if no more stones remain


print(last_stones([2,7,4,1,8,1]))
        