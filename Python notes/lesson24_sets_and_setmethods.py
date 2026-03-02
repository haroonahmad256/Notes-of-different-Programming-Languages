#Set is also an important datatype in phyton
#It is unordered collection of data items
#It is not sure that it will maintain the order of elements in set
s = {2, 4, 2, 6}     #After printing this order can be 2264 so it is unordered
print(s)

#It don't accept repititive values and if they exist it skips those values
info = {"Carla", 19, False, 5.9, 19}
print(info)
#We can't change sets like list

harry = set()    #It is a null set
print(type(harry)) 

for value in info:
  print(value)