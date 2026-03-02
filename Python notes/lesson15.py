#Function Arguments
#There are mainly four types of arguments in functions 
#First type we discuss is Default Arguments
#Default Arguments:
def mname(Fname="HAroon", Sname="AHmad", Tname="Arshad"): 
    print("I am", Fname,Sname,Tname)

mname("Ami") #Other two places will be filled automitically bcoz they are set default

#Keyword arguments
'''We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. 
Hence, the the order in which the arguments are passed does not matter.'''
def key(Fcountry="China", Ecountry="India", Ncountry="Afghanistan"):
    print("Hey", Fcountry, Ecountry, Ncountry)

key(Ecountry= "wood", Ncountry="plastic", Fcountry="Metal")
#Variable-length arguments:
'''Sometimes we may need to pass more arguments than those defined in the actual function. 
This can be done using variable-length arguments.
There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. 
The function accesses the arguments by processing them in the form of tuple.'''
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")



'''Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. 
The function accesses the arguments by processing them in the form of dictionary.'''
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")



#required argument
def name(fname, mname, lname): #These are required argument which we have to give value in all cases
    print("Hello,", fname, mname, lname)

name("Peter", "Quill") #This will through error bcoz lname is required argument and we have not assigned anything to it