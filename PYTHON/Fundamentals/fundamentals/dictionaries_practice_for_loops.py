#Create a dictionary
my_dict = {
    "name" : "nathan perry",
    "age":33,
    "fav_color": "yellow",
    "likes_dogs":True,
}

#iterate through dictionary and return the keys
for each_key in my_dict:
    print(each_key)

#print the values for each key
for each_key in my_dict:
    print(my_dict[each_key])

#Other Ways to iterate through dictionaires
#Create a new Capitals dictionary: 
capitals={
    "California" : "Sacramento",
    "Nevada": "Carson City",
    "Alaska":"Juneau",
    "Hawaii":"Honolulu",
    "Texas":"Austin",
    "Florida":"Tallahasee"
}
#iterate through all keys a new way: 
for key in capitals.keys():
    print("key here: " + key)

for value in capitals.values():
    print("Value here: " + value)

for key, value in capitals.items():
    print(key + " = " + value)


#_____________________________________________  

#Nested and Nesting
#create a list of dictionaries
users = [
    {"first_name": "penny", "last_name":"marshall"},
    {"first_name": "joe", "last_name":"shmo"},
    {"first_name": "Sal", "last_name":"mars"},
    {"first_name": "king", "last_name":"larry"}
]

#access the last name of the third user
print(users[2]["last_name"])