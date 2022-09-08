class User:     #creates a new classs. (remember class names start with an upper case letter)
    def __init__(self): #becomes the instructions on how to create new instances. (i think of it as creating the header row in the table with default values);
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 20

#now, in the outter scope, create a variable and assign it the class User. 
user_ada = User()
#then you can call on the newly created instance/record by using dot notation. 
print(user_ada.first_name)

#you can add another user if you like but it will pull the same values. 
user_2 = User()
print(user_2.first_name)

#---------------------------------------
#SETTING ATTRIBUTES 

#build a new class for storing data about shoes
class Shoes:  #decleared a new class. 
    def __init__(self): #this init method will now give instructions on how to treat each new instance. "self" is a reference to the instance, not the class. 
        self.brand = "Addidas"
        self.type = "Classic sk8-hi"
        self.price = "$69.99"
        self.in_stock = True
#the above four lines set up attributes, (columns, if thinking in table terms) for this class. Then for each attribute, assigned a default value. (So the .brand default value is "Addidas")
#now create instances of shoes outside of the scope of the class. 
my_shoes = Shoes()
dress_shoe = Shoes()
#in the above two lines, two instances are created with default values equal to those we set earlier.
#but now we can change the attributes of each instance....
my_shoes.type = "running"
dress_shoe.type = "fancy"

print(my_shoes.type)
print(dress_shoe.type) 
#it worked!    :-)

#if we do not want each instance created to have the same default values, we would pass in arguments in the init method. 

class ShoeWithArgs:
    def __init__(self, brand, type, price, in_stock):
        self.brand = brand  #notice no quotes
        self.type = type 
        self.price = price
        self.in_stock = True

#first_shoe = ShoeWithArgs()            #this wont work because we did not pass in a brand. there is no value set for it.
#print(first_shoe.brand)                 #this will print an error. 

#so we pass in arguments
first_shoe = ShoeWithArgs("Nike", "Air_Jordans", "$99.59", "False")
#now lets see what it prints: 
print(first_shoe.price)
#it worked!!       :-)



#-----------------------------------------------
# -----METHODS-------------
#a method is basically a function within the class. What objects of that particular class can do. 

class Family:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}. Nice to meet you. ")

sister = Family("J", "R", 30, "female")
sister.introduce()



#Now, lets try to use methods to change the attributes of instances. 

class ShoesAgain:
    def __init__(self, brand, type, price):
        self.brand = brand
        self.type = type
        self.price = price

    def discounts(self, percent):   #we are creating this method as something to use when we want to do a sale and reduce prices. 
        self.price = self.price * (1 - percent) #this takes the current price and changes it to the new price. (Where the new price is the old price times the discount)


running_shoe = ShoesAgain("Nike", "Runner", 150.00)
work_shoe = ShoesAgain("Any", "Steel-Toe", 84.00)

#lets apply a discount of 25% to the runner shoes. 
running_shoe.discounts(.25) #this should apply a 25% discount to the price of the running shoe. 
work_shoe.discounts(.50) #this will discount by 50%
print(running_shoe.price)
print(work_shoe.price)
