'''A while loop in Python is a control flow statement that repeatedly executes a block of code as long 
as a specified condition remains True. It is particularly useful when the number of iterations is not 
known beforehand, and the loop needs to continue until a certain condition is met.'''

i=0      #Set variable from where the counting starts
while (i<3): #print i until it is less than 3
    print(i) #first print 0 and then go to statement below mentioned
    i= i+1     #As 0 is set in variable i so 0 will come to this statement and by 0+1= 1 it will again go to while loop
                  #And as 1 is less than 3 it will be printed. And 1 will again to condition i= i+1 and will become 2. 2 will again go to 
                  #while loop and will check is 2 less than 3. As this is true so it will be executed.
else:
    print("This is out of the while loop")
#Do while loop
#This loop usually applicable in java, c and c++
#THis loop executes one time whether the condition is true or not such as

num= int(input("Enter a number: "))
print(num)               #This is actually a do while loop which executes altleast one time whether the condition is true or not
while (num<10):
    print(num)
    num += 1
#also do while
i=int(input("Enter a number: "))
print(i)
while(i>10):
    print(i)
    i-=1
    if i<10:
        print("Your number is lower than 10")



