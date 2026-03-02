class me:
    name= "Haroon"
    role= "Student"
    country= "Pakistan"
    city= "Alipur Chattha"
    def info(self):  #self refers to the current variables of of the current same object
        print(f"{self.name} is a {self.role} who lives in {self.city}, {self.country}")

mine= me()
print(f"Your name: {mine.name}\nYour role: {mine.role}\nYour city: {mine.city}\nYour country: {mine.country}")
mine.name= "Ahsan"
mine.role= "BBA Student"
mine.info()

'''The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
It must be provided as the extra parameter inside the method definition.'''

him= me()
him.name= "Daniyal"
him.role= "College student"
him.info() #Output: Daniyal is a College student who lives in Alipur Chattha, Pakistan
#Here the him.name and him.role are the some kind of parameters of info because we have used self which points to current 
#variables of current object
