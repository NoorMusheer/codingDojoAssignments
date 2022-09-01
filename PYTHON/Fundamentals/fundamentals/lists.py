fruit = ["banana", "kiwi", "watermelon", "pineapple", "raspberry"]
print(fruit)

vegetables = ["cucumber", "lettuce", "carrot", "celery", "onion"]

all_i_eat = fruit + vegetables
print(all_i_eat)

all_i_eat.pop(3)
print(all_i_eat)

all_i_eat.append("pineapple")
print(all_i_eat)

all_i_eat.remove("cucumber") #this will remove the first item that comes up which has the given value. 
print(all_i_eat)

all_i_eat.sort() #can include parameters: reverse or key; the key is a function that would specify the sorting criteria. 
print(all_i_eat)

all_i_eat.sort(reverse=True)
print(all_i_eat)

def by_length(e):
    return len(e)
all_i_eat.sort(key=by_length)
print(all_i_eat)

# splicing
new_list = ["lets", "see", "how", "well", "this", "works"]
print(new_list[2:]) #splicing will include the first item given, but not the second. 
print(new_list[:4]) #this should include values for items at index 0, 1, 2, and 3. 
print(new_list[1:3])#this should include values for items at index 1 and 2. 

#map is a built-in python function. It will apply a function to each element in a sequence and returns a new iterator. 
#if i wanted to change all the values in the "all_i_eat" list to a True boolean, then i create a function to do that...
def make_True(items):
    items = True
    return items

#then i create a variable to be set to my new iterable and apply the map function. 
new_mapped_list = map(make_True,(all_i_eat))
print(new_mapped_list)
print(list(new_mapped_list))