#All classes have function called __init(), which is always executed when object is being initiated.



class Student:
    name = "Anonymous"
    #Parameterized constructors
    def __init__(self, name, marks): # Self parameter is the reference to the current instance of the class, and is used to access variables that belongs to class. 
        print("adding new student")
        self.name = name
        self.marks = marks
    
    def welcome(self): 
        print("Welcome student ", self.name)
    
    def get_marks(self):
        return self.marks
    

#Creating object(instance)

s1 = Student("Karan", 97) #variables are called attributes.
s1.welcome()
print(s1.get_marks())