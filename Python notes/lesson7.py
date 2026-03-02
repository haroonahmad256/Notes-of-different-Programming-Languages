#here we will discuss string slicing
#in most of the programming languages counting starts with zero
fruit = "Mango"
mangoLen = len(fruit) #len is a function used to determine the length of string
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])  #automatically adds zero before :5
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1]) #this is thus: print("fruit[len(fruit)-3:len(fruit)-1]")

# Quick Quiz:
# nm = "Harry"
# print(nm[-4:-2])
# @codewithharry
