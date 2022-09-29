# Python solution for the number of times prefix is aligned
# flips = [3,2,4,1,5]

def num_times(flips):
    counter = 0
    bit_ = '0' * max(flips)
    for i in range(len(flips)):
        bit_ = bit_[0:flips[i]-1]+'1'+bit_[flips[i]:]
        if bit_[0:i+1] == '1' * (i+1) and bit_[i+1:] =='0' * len(bit_[i+1:]):
            counter +=1 
    return counter


def num_times1(flips):
    s = 0
    ex_s = 0
    r = 0
    for i, e in enumerate(flips):
        print(i,e)
        ex_s += i + 1 
        s += e
        r += int(ex_s==s)
    return r


def numTimesAllBlue(A):
        right = res = 0
        for i, a in enumerate(A, 1):
            print(i,a)
            right = max(right, a)
            res += right == i
        return res

print(numTimesAllBlue([3,2,4,1,5]))
        