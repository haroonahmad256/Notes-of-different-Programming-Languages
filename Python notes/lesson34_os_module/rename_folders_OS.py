import os

if(not os.path.exists("programs")):
    os.mkdir("programs")

for i in range(0, 30):
    os.rename(f"programs/one{i+1}", f"programs/folder {i+1}")