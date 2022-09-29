# Python solution to plant the waters 
# plants = [2,2,3,3], capacity = 5

def watering_plants(plants,capacity):
    counter = 0
    opt = 0
    total_cap = capacity
    while counter < len(plants):
        if plants[counter] <=capacity:
            capacity -= plants[counter]
            counter +=1
            opt += 1
            print(opt)
        else:
            opt += counter
            print(opt)
            capacity = total_cap

print(watering_plants([2,2,3,3],5))

            


