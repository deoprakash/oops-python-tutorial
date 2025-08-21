'''these attributes and methods are accessible from class only and are not accessible from outside.'''

class Person:
    __name  = "Anonymous"

    def __hello(self):
        print("hello person!")
    
    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__name) -> Error
# p1.__hello() -> Error
p1.welcome() #correct