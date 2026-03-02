'''The break statement in Python is a control flow statement used to terminate the execution of a loop prematurely. 
When the break statement is encountered within a for loop or a while loop, the loop is immediately exited, and 
program execution continues with the statement immediately following the loop.'''

for i in range(1,11):
                                     
    print("5 x",i+1,"=",5*(i+1))
    
    i= i+1
    if i==5:
        break   #This is a break statement which brings us out of the loop means to say it ends the loop

'''The continue statement in Python is a loop control statement used to skip the current iteration of a loop and 
proceed to the next iteration. When encountered within a for or while loop, it immediately 
stops the execution of the remaining code within the current iteration of that loop and jumps to 
the beginning of the next iteration. '''
for l in range(7,15):
    if l==10:
        print("This is continue stateement")
        continue   #It is continue statement which skip the iteration or sequence we want
    print(5*l)

for i in range(12):
 if(i == 10):
   print("Skip the iteration")
   continue
 print("5 X", i, "=", 5 * i)
