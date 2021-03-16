import random
def randInt(min=0, max=100):
    if max < 0 or min < 0:
        return "Numbers should be greater than 0"
    if min > max:
        num = random.random() * (min-max) + max
        return round(num)
    num = random.random() * (max-min) + min
    return round(num)
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=500, max=50))
print(randInt(max=-50))
print(randInt(min=-11, max=50))

