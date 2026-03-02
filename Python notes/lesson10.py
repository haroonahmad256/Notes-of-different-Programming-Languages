import time
Time= int(time.strftime("%H"))
if (9>Time>3):
    print("Good morning sir")
elif(3>Time>9):
    print("Good afternoon sir")
else:
    print("Good evening sir")






x = int(input("Enter the value of x: "))
# x is the variable to match
match x:          #This is match case statement used to match the input statement with the matching statements
    # if x is 0
    case 0:       #The match-case statement in Python provides a structured way to compare a value against various patterns and execute corresponding code blocks.
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

