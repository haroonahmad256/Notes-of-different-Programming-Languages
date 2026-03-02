'''
Access specifiers or access modifiers in python programming are used to 
limit the access of class variables and class methods outside of class 
while implementing the concepts of inheritance.

All the variables and methods (member functions) in python are by default public. 
Any instance variable in a class followed by the "self" keyword ie. self.var_name are public accessed.



'''
#Every attribute in pyton class is private until unless we make it private or protected
class country:
    def __init__(self, name, code):
        self.__name= name #This has become private and we can't access it directly to access it we have to use name mangling
        self.__code= code
        '''By definition, Private members of a class (variables or methods) are those members 
        which are only accessible inside the class. We cannot use private members outside of class.'''

pakistan= country("Pakistan", 92)
print(pakistan._country__code) #This is the name mangling purpose of it is that no one could make changing into
                               #attributes of a class so we make it private and we can only access it using name of class
print(pakistan.__dir__()) #This will give everything in class
#Morever There is no concept of public private in python these are just conventions which people use for their
#easiness. Python is doing nothing with this 

#We can also setup getter and setter to access the private attributes of a class

