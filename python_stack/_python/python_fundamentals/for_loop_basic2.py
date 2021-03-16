# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(big_list):
    for value in range(0, len(big_list), 1):
        if big_list[value]>0:
            big_list[value]="big"
    return big_list

print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(count_list):
    positives = 0
    for value in range(0, len(count_list), 1):
        if count_list[value]>0:
            positives+=1
    count_list[value] = positives        
    return count_list

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(sum_list):
    sum = 0
    for value in range(0, len(sum_list), 1):
        sum+=sum_list[value]
    return sum

print(sum_total([1,2,3,4]))    
print(sum_total([6,3,-2]))    

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(average_list):
    sum = 0
    for value in range(0, len(average_list), 1):
        sum+=average_list[value]
    average = sum/len(average_list)    
    return average

print(average([1,2,3,4])) 

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(length_list):
    return len(length_list)

print(length([37,2,1,-9]))
print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(minimum_list):
    if len(minimum_list) == 0:
        return False
    minimum = minimum_list[0]
    for number in range(1, len(minimum_list), 1):
        if minimum_list[number]<minimum:
            minimum=minimum_list[number]
    return minimum

print(minimum([37,2,1,-9]))
print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(maximum_list):
    if len(maximum_list) == 0:
        return False
    maximum = maximum_list[0]
    for number in range(1, len(maximum_list), 1):
        if maximum_list[number]>maximum:
            maximum=maximum_list[number]
    return maximum
    
print(maximum([37,2,1,-9]))
print(maximum([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(ultimate_list):
    ultimateDictionary = {
        "sumTotal": sum_total(ultimate_list),
        "average": average(ultimate_list),
        "minimum": minimum(ultimate_list),
        "maximum": maximum(ultimate_list),
        "length": length(ultimate_list),
    }
    return ultimateDictionary   

print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(rList):
    i = 0
    for reverse in range(len(rList)-1, 0, -1):
        temp = rList[i]
        rList[i] = rList[reverse]
        rList[reverse] = temp
        i+=1
    return rList

print(reverse_list([37,2,1,-9]))