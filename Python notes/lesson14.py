'''In Python, a function is a named block of reusable code designed to perform a specific task. 
Functions promote code organization, readability, and reusability, adhering to
the "Don't Repeat Yourself" (DRY) principle.'''

#Functions
def multiply(a,b): #def is for making functions and multiply is the name of function you can choose name of function
    number= a*b    #It shows the process that this function will perform
    print("Multiplication of two number",a,"and",b,"is",number)  #It also under the process these three lines are name and process of function 

a=int(input("Enter a number: "))
b= int(input("Enter second number: "))
multiply(a,b)

c=5
d= 0
multiply(c,d)

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass #it is some kind of pausing the function if we don't write it, it will throw an error
  
a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)

