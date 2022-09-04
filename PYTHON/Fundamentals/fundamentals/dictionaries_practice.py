#create a user id info dictionary
user_id = {
    "first_name" : "Adam", 
    "last_name" : "Scott", 
    "age" : 37, 
    "email" :"a.scott@anywhere.com", 
    "fav_color" :"blue",
    "is_organ_donor" : True
}


#create an empty dictionary
capitals = {}
#add values to the empty dictionary
capitals["USA"] = "Washington D.C."
capitals["California"] = "Sacramento"
capitals["Spain"] = "Barcelona"
print(capitals)

#chang the value of one of the keys in the user id dictionary
user_id["fav_color"] = "red"
print(user_id)

#only make a change to a key, if that key does not already exist
if "USA" not in capitals:
    capitals["USA"] = "this is wrong"
print(capitals)

#Accessing Values
full_name = user_id["first_name"] + " " + user_id["last_name"]
print(full_name)

#Removing Values
#capitals.pop("") will remove the last key value pair in the dictionary
#del capitals[""] will remove the key value pair for the specified key

#useful dictionary methods
#.clear() - - will remove all key value pairs in the given dictionary
#.get(key,default=none). a way to get a value. if no key exists, then it will return none. 
#  https://www.w3schools.com/python/python_ref_dictionary.asp




