#typecasting is a method to change the type of variable means float to ineger

"""The conversion of one data type into another data type, done via developer or 
programmer's intervention or manually as per the requirement, is known as explicit type conversion."""
a= "1"
b="3" 
print(int(a)+int(b))     #this is explicit type casting which is done by us manually

'''Implicit TypeCasting is done by python it self such as
Python converts a smaller data type to a higher data type to prevent data loss.'''

c = 1.9  #which is float
d = 8 #integer

print(c + d) #float+integer

print("The type of c is", type(c))


