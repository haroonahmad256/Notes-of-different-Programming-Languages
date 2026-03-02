import os

if(not os.path.exists("programs")):
    os.mkdir("programs")

for i in range(0,30):
    os.mkdir(f"programs/question{i+1}") #To create 30 program files
