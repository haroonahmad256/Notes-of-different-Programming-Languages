# Input a number from user
num = int(input("Enter an integer: "))

#conditional operators
# Simple if structure (no else)
# > uses for greater than
# < uses for less than
# == for equivalance
# >= greater than or equal to
# <= less than or equal to
# != not equal to
#If- else is conditional statement

if num % 2 == 0:
    print("The number is even")
    print("Pakistn") #it is also in if

else:
    print("The number is odd")
    print("it is also in else condition")
print("india") #It is not in else condition

MarksPf= int(input("Enter your marks in programming fundamentals: "))
MarksDst= int(input("Enter your marks in discrete structures: "))
Total= MarksDst+MarksPf
Average= Total/2
CGPA= Total/400
if(MarksPf>50):
    print("You have passed in programming fundamentals")
elif(MarksDst>50): #This is elif which can be generally used in between if and else and it is used to make more conditions and possiblities
    print("You have also passed in discrete structures")
elif(Total>160): #we can put multiple elif between if and else
    print("Your CGPA is",CGPA)
else:("You have failed")

applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

    num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")


num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10): #we can also put further if in elif
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")