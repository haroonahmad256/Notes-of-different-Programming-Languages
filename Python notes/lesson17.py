l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
print(l.append(7)) #this append method adds a given number at the end of list
print(l.sort(reverse=True)) #this method is used to arrange elements of list order wise
print(l.reverse()) #It reverse the order of list l
print(l.index(1)) #It gives number of the index we want
print(l.count(1)) #It will count how may there are 1 in list
m = l.copy() #It will make m a copy of list l
m[0] = 0
print(l.insert(1, 899))
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m)
print(l)

m.remove(1000)    #It removes the element mentioned in list
print(m)
m.pop(0)    #it also removes the element on given index
print(m)
m.insert(1, "harry") #This method wil add "harry" at index 1 but it will not replace it will hold the place chaging index of others
print(m)
del m[0]    #used to delete a element at given index
print(m)
m.clear()      #remove all elements of string
print(m)

