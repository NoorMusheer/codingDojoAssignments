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