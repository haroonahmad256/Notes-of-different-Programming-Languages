#List 
'''Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation.'''
list1= [6, 5, 9, "haroon", "Pakistan"]
print(list1)
print(len(list1))
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[len(colors)-5]) #=
print(colors[3])
#print(list1[5])  #will through an error because 5 index does not exist

Stationary = ["Pen", "Pencil", "rubber", "eraser", "remover"]
if "Pen" in Stationary:
    print("Pen is present.")
else:
    print("Yellow is absent.")

if "whitener" in Stationary:
    print("whitener is present")
else:
    print("Whitener is not present")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith = [item for item in names if "o" in item]
print(namesWith)

math= ["calculus", "geometory", "analytics"]
myth= [component for component in math if "c" in component]
print(myth)


