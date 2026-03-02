#This is for else loop
for i in range(10):
    print(i)
    if(i==5):
        print(i)
        break            #As here loop has been breaked so else will not execute
else: #it will be executed when loop is completely finished in 
      #this case it will be printed when loop run till i=10
    print("is this will be executed")
#The content inside will be excuted when for loop is completely finished and there is no break

