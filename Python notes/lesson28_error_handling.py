#To avoid and handle errors in python we do error handling
#We use this beacause we don't want our program to hold or stop in middle of program
#If error occurs we give another direction to program by using this method
#This is done using try except method

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

finally:  #in finally code always executes irrespective of try and except
   print("Some imp lines of code")
   print("End of program")
   



try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

finally:
   print("This will always be executed") 
   #Why we need this finally keyword when we can write like this?
print("This will be executed always")
#It is mostly needed in function when we return a value 1 or 0 the code after it will not be exucted but if we
#have used finally key word whether we have returned some value the code in finally always be executed irrespective of what is condition
#like
def integer():
  try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
    return 1
  except ValueError:
      print("Number entered is not an integer.")
      return 0
      
  except IndexError:
    print("Index Error")
    return 0

  finally:
    print("This will always be executed") 
  
  print("This will be executed always")  #This line will not be executed because it is not in finally and a value has been returned
  
