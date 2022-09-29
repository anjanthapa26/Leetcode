from itertools import chain
def kWeakestRows(mat, k):
    def num_ones(L):
        beg, end = 0, n
        while beg < end:
            mid = (beg + end)//2
            if L[mid] > 0: 
                beg = mid + 1
            else: 
                end = mid
        return beg
    
    m, n = len(mat), len(mat[0])
    buckets = [[] for _ in range(n+1)]
    print(buckets)
    for i, row in enumerate(mat):
        buckets[num_ones(row)].append(i)
        print(buckets)

        
    return list(chain(*buckets))[:k]

print(kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))