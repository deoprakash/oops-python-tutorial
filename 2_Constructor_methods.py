# #All classes have function called __init(), which is always executed when object is being initiated.



# class Student:
#     name = "Anonymous"
#     #Parameterized constructors
#     def __init__(self, name, marks): # Self parameter is the reference to the current instance of the class, and is used to access variables that belongs to class. 
#         print("adding new student")
#         self.name = name
#         self.marks = marks
    
#     def welcome(self): 
#         print("Welcome student ", self.name)
    
#     @staticmethod  #static method is used to convert a normal method to static by removing self parameter.
#     def college():
#         print("ABC College")
    
#     def get_marks(self):
#         return self.marks
    

# #Creating object(instance)

# s1 = Student("Karan", 97) #variables are called attributes.
# s1.welcome()
# s1.college()
# print(s1.get_marks())

#--------------------------------------- Class method ---------------------------------

# class Person:
#     name = "Anonymous"

#     # def changeName(self, name):
#         # self.name = name # -> change name only inside the method  
#         # Person.name = name # -> change name of class attribute.

#         #------ Alt Method of change name ----------
    
#     # def changeName(self, name):
#     #     self.__class__.name = name

#         #------ Alt Method of change name ----------
    
#     @classmethod
#     def changeName(cls, name): # -> cls is referring to class not self
#         cls.name = name

# p1 = Person()
# p1.changeName("ABC")
# print(p1.name)
# print(Person.name)