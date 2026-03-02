#Here we will discuss about dictionories
'''Dictionaries are ordered collection of data items. 
They store multiple items in a single variable. Dictionary items are key-value pairs 
that are separated by commas and enclosed within curly brackets {}.'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name']) #name is a key and this will give the value of name which is karan
print(info.get('eligible')) #This also do the same thing
 
print(info.keys()) #This will give the only keys in dictionries
print(info.values()) #This will only values of keys 
print(info.items()) #This will give both keys and values

for key in info.keys(): 
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 

#Dictionaries methods
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2) #contcatinate ep2 to ep1
ep1.update('190':90)
ep1.clear() #clear all the key value pairs inside ep1
ep1.pop(122)  #remove key value pair of 122
ep1.popitem()   #remove last key value pair
del ep1[122]  #remove key value 122 pair
del ep1       #completely delete dict
print(ep1) 