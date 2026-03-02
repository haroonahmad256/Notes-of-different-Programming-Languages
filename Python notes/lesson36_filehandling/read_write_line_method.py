f = open('operatable_file.txt', 'r')
i=0
while True:    #THis will continue till lines doesn't come to end
    i+=1
    line = f.readline()
    numbers= line.split(",")  #This split method will convert data of first line into a list wow!
    if not line:
        break
    print(f"Marks of student {i} in Math: {numbers[0]}")
    print(f"Marks of student {i} in Bio: {numbers[1]}")
    print(f"Marks of student {i} in Urdu: {numbers[2]}")
    #the data stored in numbers and line is stored as string so to convert into other type we have to type cast it
    print(f"Total marks of student {i} is {(int(numbers[0])+int(numbers[1])+int(numbers[2]))} with average of {(int(numbers[0])+int(numbers[1])+int(numbers[2]))/3} and percentage of {((int(numbers[0])+int(numbers[1])+int(numbers[2]))/300)*100}")
f.close()

f2 = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f2.writelines(lines)
f2.close()    