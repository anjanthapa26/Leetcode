#Python solution to find the smallest number greater than target.
# letters = ["c","f","j"], target = "a"


def next_greater(letters,target):

    d= {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
    'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'x':23,'y':24,'z':25}

    low = 0
    high = len(letters)
    while low < high:
        mid = (low + high) //2
        print(mid)
        if d[target] < d[letters[mid]]:
            high = mid 
        else:
            low = mid + 1

    if low == len(letters):
        return letters[0]

    return letters[low]

print(next_greater(['c','f','g'],'z'))