# '''
# In Python, the map, filter, and reduce functions are built-in functions that allow you 
# to apply a function to a sequence of elements and return a new sequence. 
# These functions are known as higher-order functions, as they take other functions as arguments.
# '''

# '''
# The map function applies a function to each element in a sequence and returns a new 
# sequence containing the transformed elements. The map function has the following syntax:

# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. 
# The iterable argument can be a list, tuple, or any other iterable object.'''

# def cube(x):
#     return x*x*x

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Double each number using the map function
# doubled = map(lambda x: x * 2, numbers)   #passing function as an argument
# c= list(map(cube, numbers))
# #map(name_of_function, list_on_which_you_want_apply_the_function_on_every_member_of_list)
# #Print the doubled numbers
# print(list(doubled))
# print(c)

# '''
# The filter function filters a sequence of elements based on a given predicate 
# (a function that returns a boolean value) and returns a new sequence containing 
# only the elements that meet the predicate. The filter function has the following syntax:

# filter(predicate, iterable)
# The predicate argument is a function that returns a boolean value and is applied 
# to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.
# '''

# def is_greater(x):
#     return x>2

# newewl= filter(is_greater, numbers) #passing function as argument
# #filter(function_on_basis_of_which_numebers_in_the_list_would_be_classified, list_of_numebers_on_which_filter_function_to_be_applied)
# print(list(newewl))

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Get only the even numbers using the filter function
# evens = filter(lambda x: x % 2 == 0, numbers)

# # Print the even numbers
# print(list(evens))

'''
The function argument is a function that takes in two arguments and returns a single value. 
The iterable argument is a sequence of elements, such as a list or tuple.
The reduce function applies the function to the first two elements in the iterable and 
then applies the function to the result and the next element, and so on. 
The reduce function returns the final result.
'''
from functools import reduce
def factorial(x):
    f=1
    for i in range(x, 1):
        f*= (i)
    return f

# List of numbers
numbers = [1, 2, 3, 4, 5]
fact= map(factorial, numbers)
print(list(fact))

# # Calculate the sum of the numbers using the reduce function
# sum = reduce(lambda x, y: x + y, numbers)
# #reduce(function_to_apply_on_each_element_of_list, list)
# # Print the sum
# print(sum) #15 will be printed