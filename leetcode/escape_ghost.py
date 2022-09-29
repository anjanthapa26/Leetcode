# Python solution to escape ghost 
# ghosts = [[1,0],[0,3]], target = [0,1]

def escape_ghost(ghosts,target):
    dest = abs(target[0]) + abs(target[1])

    for ghost in ghosts:
        dist = abs(target[0]-ghost[0]) + abs(target[1]-ghost[1])

        if dist <= dest:
            return False

    return True
