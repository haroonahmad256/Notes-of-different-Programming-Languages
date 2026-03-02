#in this lesson we will discuss about tuple
#The main difference between list and tuple is that tuples are unchangeable.
tuple1= ("pakistan", "india", "bangladash") #This is a tuple
print(tuple1)

names= ("Haroon") #This is an ordinary string
names= ("Haroon",) #but this is tuple
print(type(names))

#to find thelength of tuple
lengt= len(tuple1)
print(lengt)

#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
#we can also do slicing in case of tuple

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#To make changes in a tuple we must convert it to list and then we can make changes
countries= ("Iran", "Iraq", "Uae", "Saudi Arabia")
list1= list(countries)
another_country= "Oman"
list1.append(another_country)
print(list1)
list1.pop(2)
print(list1)

countries= tuple(list1)
print(countries)
#To delete the entire tuple
del countries
