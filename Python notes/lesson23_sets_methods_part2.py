# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. 
# This method returns False if items are present, else it returns True.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))#False

#issuperet
#Checks if first set contain all elements of second set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

#issubset
#checks if first set is subset of other set means first set contain elements which are also in secod set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()
# If you want to add a single item to the set use the add() method.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# update()
# If you want to add more than one item, simply create another set or any 
# other iterable object(list, tuple, dictionary), and use the update() method 
# to add it into the existing set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# remove()/discard()
# We can use remove() and discard() methods to remove items form list.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
#If item is not present remove() will raise error
#While discard will not raise error it will return None

# pop()
''' This method removes the last item of the set but the catch is 
that we don't know which item gets popped as sets are unordered. 
However, you can access the popped item if you assign the pop() method to a variable.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities) #It will throw error because cities has been deleted

# clear():
# This method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if item exists
# You can also check if an item exists in the set or not.
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
