# Python solution for the binary watch 
# turnedOn = 1


def binary_watch(turnedon):
    opt = []
    for hrs in range(0,12):
        for min_ in range(0,60):
            if (bin(hrs) + bin(min_)).count('1') == turnedon:
                time = '%d:%02d'%(hrs,min_)
                opt.append(time)
    return opt


print(binary_watch(1))
