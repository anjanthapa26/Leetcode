# Python solution to insert an interval
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

def insert(intervals,newInterval):
    i = 0
    opt = []
    merge_arr = []
    flag = 0
    while newInterval[1] >= intervals[i][1]:
        if newInterval[flag] >= intervals[i][flag]:
            i +=1
        else:
            i -=1
            merge_arr.append(intervals[i][flag])
            flag = 1
            opt += intervals[:i]
    merge_arr.append(intervals[i][flag])
    opt += [merge_arr] + intervals[i+1:]
    return opt


# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# intervals = [[1,3],[6,9]], newInterval = [2,5]
# intervals = [[2,4],[5,6]], newInterval = [0,1]
def insert(intervals,newInterval):


print(insert([[1,3],[6,9]],[2,5]))
        



