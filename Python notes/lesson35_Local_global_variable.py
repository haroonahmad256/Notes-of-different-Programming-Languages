a= 90  #Global variable

def addition():
    b= 3   #Local variable
    a=84   #Local variable
    print(a+b)

addition()
print(a)
#print(b) #This will give a error because local variable can only accessed in the function not outside the function
#For example if we want to change the value of global variable in a function we will use global keyword

def sub():
    c= 32
    global a    #It change the variable of global scope and modifies the global variable
    a= 8
    print(c-a)

sub()
print(a)   #Now value of a will be 8 instead of 90