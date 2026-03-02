'''"for loops" can iterate(the process of repeating a set of instructions or a block of code in programming) over a 
sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, 
lists, tuples, sets and dictionaries. iterable objects are those on which for loop can be applied for example list or string'''

FirstList= ("Haroonn Ahmad", "Pakistan", "Muslim")  #It is a list
for character in FirstList: #for loop will print elements of list one by one 
    print(character) #gives elements in list
    for gh in character: #This is for in for loop   'this is nested loop
        print(gh) #gives every character of every element of list


for L in range(2): #it will give all the number between O and 29999 and it always start from O
    print(L)

for H in range(1,9): #it don't include 9 but include 1 if one was not written it will start from O
    print(H)


for t in range(1,8,8): #it will omit or strip or disappear 8 elements or numbers between 1 and 8
    print(t)

for v in range(1,59,4): #it will always remove 4 number after 1 and will write 5th number and will continuously repeat this process
    print(v)
for x in range(8,44,5): # Will remove 5 number after 8 and will print 6th number afeter 8 wich is 14
    print(x)
    



# name = 'Abhishek'
# for i in name:
#   print(i)
#   if(i =="b"):
#     print("This is something special!")
    
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#   print(color)
#   for i in color:
#     print(i)

# for k in range(5):
#   print(k + 1)
  
# for k in range(1, 20001):
#   print(k)

  
for k in range(1, 12, 3):
  print(k)