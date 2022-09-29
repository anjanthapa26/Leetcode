# Python program to water a plant
#  plants = [2,2,3,3], capacity = 5

def water_plants(plants,capacity):
    opt = 0 
    counter = 0
    flag = False
    total_cap = capacity
    while counter < len(plants):

        if plants[counter] <= capacity:
            capacity -= plants[counter]
            counter +=1
            if flag:
                opt += counter
                flag = False
            else:
                opt +=1
        else:
            flag = True
            opt += counter 
            capacity = total_cap

    return opt


print(water_plants([1,1,1,4,2,3],4))

        
        



