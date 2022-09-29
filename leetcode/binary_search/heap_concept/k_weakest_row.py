#Python solution to find the k weakest row in matrix
# mat = 
#[[1,1,0,0,0],
# [1,1,1,1,0],
# [1,0,0,0,0],
# [1,1,0,0,0],
# [1,1,1,1,1]], 
#  k = 3


def k_weakest(mat,k):
    l = len(mat)
    opt = []
    checker = 0
    for i in range(l):
        if not opt:
            opt.append((mat[i].count,i))
        else:
            curr = (mat[i].count,i)
            print(curr[0],opt[checker][0])
            while curr[0] < opt[checker][0]:
                if curr[0] == opt[checker][0]:
                    opt.insert(checker,curr)
                checker -=1
                if checker == -1:
                    opt.insert(0,curr)

            while curr[0] > opt[checker][0]:
                if curr[0] == opt[checker][0]:
                    opt.insert(checker,curr)
                checker +=1
                if checker == len(opt):
                    opt.append(curr)
    return opt


print(k_weakest([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))



            

        