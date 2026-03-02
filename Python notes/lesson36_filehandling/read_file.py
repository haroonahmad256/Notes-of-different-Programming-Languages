'''Before we can perform any operations on a file, 
we must first open it. Python provides the open() function to open a file. 
It takes two arguments: the name of the file and the mode in which the file should be opened. 
The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.'''

f= open("operatable_file.txt", "r") 
#r mode is the default mode in python even if we don't write it, it will be opened in r mode by default moreever
#we can also write 't' with 'r' as it specify that we are opening a text file 'read_text' but it is no need of it because
#it is by default wherease if we write 'rb' it will be opened in binary mode and content in file would be read in form of bytes
#rb is used when we have to open a jpeg, pdf, exe or other file.
content= f.read()
print(content)
f.close()