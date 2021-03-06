# Create a Python file called for_loop_basic1.py that performs the following tasks.

# Basic - Print all integers from 0 to 150.
for all in range (0, 151, 1):
    print(all)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for five in range (5, 1000, 5):
    print(five)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for dojoWay in range (1, 101, 1):
    if dojoWay%10 == 0:
        print("Coding Dojo")
    elif dojoWay%10 == 0:
        print("Coding")
    else:
        print(dojoWay)        

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for odd in range (1, 500001, 2):
    sum += odd
print(sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for countdown in range (2018, 0, -4):
    print(countdown)
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for flexible in range (lowNum, highNum+1, 1):
    if flexible%mult == 0:
        print(flexible)