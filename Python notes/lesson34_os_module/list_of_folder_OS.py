import os
folders= os.listdir("programs")

for i in range(0,30):
    print(folders[i])

#This can be also done by this
print(os.getcwd()) #It gives current directory or file address in which we are working
os.chdir("/python programming")  #This function changes the directory to sepcific directory
print(os.getcwd())        #get current working directory (getcwd)

for folder in folders:
    print(folder)
    print(os.listdir(f"programs/{folder}"))

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']