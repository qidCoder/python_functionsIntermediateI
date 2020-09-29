#Created by Shelley Ophir
#Coding Dojo Sep. 29, 2020
#With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.
    # If no arguments are provided, the function should return a random integer between 0 and 100.
    # If only a max number is provided, the function should return a random integer between 0 and the max number.
    # If only a min number is provided, the function should return a random integer between the min number and 100
    # If both a min and max number are provided, the function should return a random integer between those 2 values.
    #BONUS: account for any edge cases (eg. min > max, max < 0)

#import the random library
import random

def randInt(min=None, max=None):
    if (min == None and max == None):
        return round(random.random()*100)
    elif (min == None and max != None):
        if (max < 0):
            max = abs(max)

        return round(random.random()*max)
    elif (min != None and max == None):
        if (min < 0):
            min = abs(min)

        return round(random.random() * (100 - min) + min)
    else:
        if (max < 0 or min < 0):
            max = abs(max)
            min = abs(min)
        if (min > max):
            temp = min
            min = max
            max = temp
        return round(random.random() * (max - min) + min)
    
print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print(randInt(min=-50, max=-500))    # should print a random integer between 50 and 500, accounting for edge cases