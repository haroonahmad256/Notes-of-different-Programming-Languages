#String Methods
a= "@@Haroon@@@" #strings are immutable cannot be changed
print(a.upper) #For upper case characters which are stored in variable
print(a.lower) #For lower case characters which are stored in variable
#These don't change existing string whether it forms another string
print(a.rstrip("@")) #if @ was written in end of string this strip function would strip or disapper that sign
print(a.replace("Haroon", "Ahmad")) #replaces text in the string
print(a.split(" ")) #split or separate the text
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) #capatalize the whole string

str1 = "Welcome to the Console!!!"
print(len(str1)) #length of str1 is 25
print(len(str1.center(50))) #align the string in center. 
# here string length was 25 so it added 25 spaces to align it in center
print(a.count("Haroon"))  #count the number of occuring things in string

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) #this endswith tell check whether the string is ending with th specific word or sign

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) #4 and 10 are slicing and specifi that between 4 and 10 string is ending with "to"

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh")) #use to find certain text or something else if that thing is not found it returns -1
# print(str1.index("ishh")) # this is index method similar to find method but it return error when something is not present

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) #this method returns true when string is made of A-Z or a-z or 1-9 numerics otherwise it return false
str1 = "Welcome"
print(str1.isalpha()) #this do not include 1-9 number and include A-Z and a-z if it include 1-9 it return false


str1 = "hello world"
print(str1.islower()) #check if string in lower case

str1 = "We wish you a Merry Christmas\n" 
print(str1.isprintable()) #this method checks if the string is printable
str1 = "         "       #using Spacebar
print(str1.isspace()) #check if the string contain white spaces if string contain it, return true
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle()) #check if the string is in title form

str2 = "To Kill A Mocking Bird"
print(str2.istitle()) #check if every word of string is capatalize

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python")) #check if the string is starting with specific word or sign

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #interchang the case of every character of string

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) #It make the string a title every word has large alphabet


