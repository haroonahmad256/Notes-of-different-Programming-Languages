with open("myfile.txt", 'r') as f:
    f.seek(10)      #seek method is used to start reading file from a specific location
                    #Here reading starts when 10 bytes reached
                    #means if file contain "Hello this file is reading" here we see the 10th character is 's'
                    #so 's' will be skipped and reading will be started from ' fi'. Readed data:  file is reading
                    #unreaded: Hello this
    print(f.tell()) #IT will give the position from where reading starts here we have seeked 10 so tell will give 10
    data= f.read(5)       #here we also have set the limit means this read method will read only 5 character or bytes
    print(data)

with open("myfile.txt", 'a') as f2:
    f2.write("Hello how are you")
    f2.truncate(5)    #This limits the data written in file by this method only 5 characters would be written in file and we can change this limit as we wish
                      #only Hello is written in file
