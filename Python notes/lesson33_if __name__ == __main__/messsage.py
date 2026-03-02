def heloo():
    print("This is a new message")

name= "New"
print(__name__)   #This will tell whether the file is running in main file or from another source as a module
if __name__ == "__main__":   #This is condition which is saying that only run below code if this file is running directly not from 
                             #another file in form of import and using this program will not run two times it is important when working
                             #on large project and you have to run program in each file in this way you can implement this condition to avoid conflicts
    print(name) 
    heloo()