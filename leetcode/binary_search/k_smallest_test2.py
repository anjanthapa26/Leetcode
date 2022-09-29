def k_smallest(mat,k):
    m, n = len(mat), len(mat[0])
    result = {}
    for j in range(n):
        for i in range(m):
            if mat[i][j] or i in result: continue
            result[i] = True
            k -= 1
            if not k: return result.keys()
            print(result)
    for i in range(m):
        if i not in result:
            result[i] = True
            k -= 1
            if not k: return result.keys()

print(k_smallest([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))
        