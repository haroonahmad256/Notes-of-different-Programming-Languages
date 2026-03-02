'''
The enumerate function is a built-in function in python to loop over a sequence 
such as (list, tuple, or string) and get the index and the value of each element 
in the squence at the same time
'''
classmates= ["Aqsam", "Khan","Yawar", "Rohan", "Daniyal", "Haroon", "Yaseen", "Siraj"]
for i, mates in enumerate(classmates):
    print(i,":",mates)
    if(i==5):
        print("He is a genius")

#Here i is index and mates is the value
#index is always written first and then the variable in which value at certain index to be stored
#Enumerate return a tuple containing the index and value of each element in the sequence
#usually index starts from 0 but if we want it start from sepcific number such as from 1 then we can do this

for i, mates in enumerate(classmates, start=1):
    print(i,":",mates)
    if(i==5):
        print("He is a genius")