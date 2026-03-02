#import in python is a process of loading code from a python module into current script.
#This allows you to use functions and variables defined in the module in your current script as well
#as any additional module that imported modules depends upon
import pandas  #All code in pandas is now mine and i can use it using different functions
import math
#pandas.read_csv()  #This is a function which reads csv files and we can give file name as argument
print(pandas.__version__)
print(math.floor(4.32333))
result = math.sqrt(9)
print(result)  # Output: 3.0
#if we want import not the whole module only some functions from module we can write it like this
from math import sqrt, pi #here we extracted sqrt and pi from math and now can we use it like this
new= sqrt(16) * pi
print(new)

# importing everything
# It's also possible to import all functions and variables from a 
# module using the * wildcard. However, this is generally not recommended as 
# it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
from math import *
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793

import math as m #for convinient writing
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793

from math import sqrt as s;
faa= s(34)

#Finally, Python has a built-in function called dir that you can use to 
#view the names of all the functions and variables defined in a module. 
#This can be helpful for exploring and understanding the contents of a new module.

import math
print(dir(math)) #list all the functions in math

#We can also make our own import files like
from lesson32_import_file import addition, myname #if we use * it will import everything from it
addition()
print(myname)

