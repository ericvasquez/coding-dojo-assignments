# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
print(x)
students[0].update({"last_name": "Bryant"})
print(students)
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
z[0].update({"y": 30})
print(z)

# Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(0, len(some_list), 1):
        for key, val in some_list[i].items():
            print (key + " - " + val)
iterateDictionary(students) 


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for name in some_list:
        print(name[key_name])
iterateDictionary2('first_name', students)

def iterateDictionary2(key_name, some_list):
    for name in some_list:
        print(name[key_name])
iterateDictionary2('last_name', students)


# Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
 for key, value in dojo.items():
    print(len(value), key.upper())
    for i in range(0,len(value), 1):
        print(value[i])

printInfo(dojo)

