# Python solution to create a letter case permutation
# s = "a1b2"


def letter_case(s):
    opt = [""]
    for i in s:
        temp = []
        if i.isalpha():
            for o in opt:
                temp.append(o + i.lower())
                temp.append(o + i.upper())
        else:
            for val in opt:
                temp.append(val+i)
        opt = temp
    return opt



print(letter_case('a1b2'))
