#now we will discuss strings
#we know it is a data type and anything which is enclosed in double quotes is called string data type
#single quotes can also be used to make strings
print("code with harry")


#to make multi line string we use triple single quote or triple double quotes such as
print('''Hello ahsan!
      how are you?
      where are you?''')



#strings examples

apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''
 
#string slicing

print(apple[0]) #gives first charactar of the string name
print(apple[1]) #gives second charactar of the string name
print(apple[2]) #gives third charactar of the string name
print(apple[3]) #gives fourth charactar of the string name
print(apple[4]) #gives fifth charactar of the string name
# print(name[5]) # Throws an error becaue it do not exist


print("Lets use a for loop\n")

for character in apple:    #it is a loop and this one loop is used to print charactar one by one in string apple
    print(character)       #in vertcal manner

he= "Pakistan"
for character in he:
    print(character)
