#Section 1 given code: 
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

#part 1:Change the value 10 in x to 15
x[1][0]=15

#part 2: Change the last name of the first student from "Jordan" to "Bryant"
students[0]["last_name"]="Bryant"

#part 3: in the sports_dictionary change Messi to Andres.
sports_directory["soccer"][0] = "Andres"

#part 4: Change the value of 20 in z to 30
z[0]["y"]=30

#-------

#Section 2. 
#create a function that given a list of dictionaries, it iterates through and prints each key and the associated value. 

def iterate_dict(students):
    for i in students:
        print("first_name - " + i["first_name"], ", last_name - " + i["last_name"])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterate_dict(students)

#----------

#Section 3
#Create a function that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

def iterate_dictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterate_dictionary2("first_name", students)
iterate_dictionary2("last_name",students)

#----------
#Section 4:
#Iterate Through a Dictionary with List Values -Create a function that, given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
def print_info(some_dict):
    for key in dojo.keys():
        print(str(len(some_dict[key])) + " "+ key)
        for i in some_dict[key]:
            print(i)
    

dojo = {
    'LOCATIONS': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'INSTRUCTORS': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print_info(dojo)
