# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Eric"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 13
print("Hello", name)	# with a comma
# print("Hello " + name)	# with a +	-- this one should give us an error!
print("Hello " + str(name))
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "cheeseburgers"
fave_food2 = "pizza"
print("I love to eat {}".format(fave_food1)) # with .format()
print("I love to eat {}".format(fave_food2)) # with .format()
print(f"I love to eat {fave_food1}") # with an f string
print(f"I love to eat {fave_food2}") # with an f string


print("I love to eat {0} and {1}".format("sushi", "pizza")) # with numbered indexes
print("I love to eat {1} and {0}".format("sushi", "pizza")) # numbered indexes in a different order

print("I love to eat {fave_food1} and {fave_food2}".format(fave_food1 = "sushi", fave_food2 = "pizza")) #with named indexes
