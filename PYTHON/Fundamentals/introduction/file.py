num1 = 42 #variable declaration, Interger
num2 = 2.3 #variable declaration, float
boolean = True #variable declaration, Boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, class
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple? 
print(type(fruit)) #display variable type of the fruit variable
print(pizza_toppings[1]) #display the list of pizza toppings stored in the variable. 
pizza_toppings.append('Mushrooms')#add "Mushrooms" to the pizza_toppings list. 
print(person['name'])#display the value of the "name" key under the person class. 
person['name'] = 'George' #set the value of the name key in the person class variable to "George"
person['eye_color'] = 'blue' #add a key-value pair to the person class with the key set to "eye-color" and the value set to "blue" 
print(fruit[2]) #display the third element in the fruit list.
if num1 > 45: #conditional, if/else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:#conditional, if/elif/else statement
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop, will display 5
    print(x)
for x in range(2,5): #for loop will display 2, 3, 4, 5
    print(x)
for x in range(2,10,3): #for loop, will display 2,5,8
    print(x)
x = 0 #while loop; will display 1,2,3,4
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #remove the last topping in the pizza_toppings list. 
pizza_toppings.pop(1) #remove the second topping in the pizza_toppings list. 

print(person) #display the attributes associated with the person class. 
person.pop('eye_color') #remove the "eye_color" attribute from the person class
print(person) #display the attributes associated with the person class again. 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for loop, go through the list of toppings, and display the topping, stop once it reaches a topping called "olives"

def print_hello_ten_times(): #create a function that includes a for loop to display "hello" ten times. 
    for num in range(10):
        print('Hello')

print_hello_ten_times() #actually runs the function above 

def print_hello_x_times(x):#creates a function that will display the string "hello" according to the value of the x variable. 
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #runs the function above and will display "hello" four times. 

def print_hello_x_or_ten_times(x = 10):#creates a function that will print "hello" several times, based on the argument passed. 
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #will run the function above and display "hello" ten times
print_hello_x_or_ten_times(4) #will run the function above and display "hello" four times. 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)