f = open('operatable_file.txt', 'w')
f.write('Hello, world!') #Hello world would be written in file
#We can also do this
 
with open('operatable_file.txt', 'a'):
    f.write("Hey go to pakistan")

#In this way we don't need to close the file
#Even if we don't want to write f then

with open('operatable_file.txt', 'a') as f:
    f.write("Hey go to pakistan")