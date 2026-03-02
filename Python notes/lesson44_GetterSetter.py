class person:
    def __init__(self, name, age, citizenship):
        self.__name= name
        self.__age= age
        self.__citizenship= citizenship

    @property
    def getName(self):
        return self.__name
    @getName.setter
    def setName(self, Name):
        self.__name= Name

    @property
    def getAge(self):
        return self.__age
    @getAge.setter
    def setAge(self, age):
        self.__age= age

    @property
    def getCitizenship(self):
        return self.__citizenship
    @getCitizenship.setter
    def setCitizenship(self, citizenship):
        self.__citizenship= citizenship
    
    
    def printInfo(self):
        print(f"{self.name} has age of {self.age} and He is citizenship of {self.citizenship}.")


firstObjectOfPerson= person("Haroon", 19, "Pakistan")
print(firstObjectOfPerson.getAge) #when we use @property which is a decorator it make the methods 
                                  #behave like an attribute so with getAge we don't have to use parathensis
firstObjectOfPerson.setName= "Bilal"
print(firstObjectOfPerson.getName)
