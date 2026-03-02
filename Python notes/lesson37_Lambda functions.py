'''
In Python, a lambda function is a small anonymous function without a name. 
It is defined using the lambda keyword and has the following syntax:
lambda arguments: expression
Lambda functions are often used in situations where a small function is required for a short period of time. 
They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
'''
def appe(n, x):
    return 6 + n(x)
#lamda function to calculate average

average= lambda a, b, c: (a+b+c)/3
print(average(45,76,98))

# Lambda function to calculate the product of two numbers,
# with additional print statement
cube= lambda d,e,f: print(f"The multiple of three numbers is {d*e*f}")
cube(45,76,98)

product= lambda a: (a*a*a)/3
print(appe(product,5))
print(appe((lambda x: x*x), 4))
