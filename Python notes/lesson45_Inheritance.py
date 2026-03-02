class Employee:
    def __init__(self, name, empNumber, Age):
        self.__name= name
        self.__empNumber= empNumber
        self.__Age= Age

    def showDetail(self):
        print(f"Employee {self.__empNumber} has name {self.__name} with the age of {self.__Age}")

    @property
    def getName(self):
        return self.__name
    
class programmer(Employee): #Inheriting programmer from Employee class
    def showLanguage(self):
        print("The default language is Python")
        

emp1= Employee("Hungry", 7831, 29)
emp1.showDetail()
emp2= programmer("Haroon", 9999, 19)
emp2.showLanguage()

