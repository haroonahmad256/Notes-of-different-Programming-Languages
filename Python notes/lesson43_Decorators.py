#Decorator is a function which is used to modify and decorate the starting and ending of program beautiful
'''
A decorator is a function that takes another function as an argument and 
returns a new function that modifies the behavior of the original function. 
The new function is often referred to as a "decorated" function.
'''

def greet(fx):      #This is modifier function which is taking function which have to modify as argument
    def new():      #This new function is to be returned with modified passed function
        print("Good Evening")
        fx()
        print("How was the experience?")
    return new

@greet
def country():  # We pass the function which we want to modify as argument 
    print("Hello My Counrty is Pakistan")

country()
