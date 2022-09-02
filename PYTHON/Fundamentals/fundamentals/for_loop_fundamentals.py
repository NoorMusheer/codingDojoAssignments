print("First Answer")
#start multi-line comment out with """ below. 
""" 
for i in range(5):
    print(i)

print("Second Answer")
for i in range (2, 7):
    print(i)


print("Third Answer")
for i in range (3,15,2):
    print(i)


print("Fourth Answer")
for i in range (10,0,-3):
    print(i)


#for loops through strings
for x in ("hello"):
    print(x)

#for loops though lists: 
my_list=["abc", "xyz", 123]
for x in my_list:
    print(x)

#While loops in range
count = 0
while count < 5:
    print(count)
    count += 1

#else functions
y = 1
while y<7:
    print(y)
    y +=1
else: 
    print("last statement")

#break within a loop
for i in ("string"):
    if i == "n":
        break
    else: print(i)

"""
#continue within a loop
for i in ("string"):
    if i == "r":
        continue
    else: print(i)

    