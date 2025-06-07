#Simple inheritance

#Base Class
class Animal:
    def __init__(self, name):
        self.name = "Buddy"
    
    def speak(self):
        print(f"{self.name} makes a sound!")

# derived class 
class Dog(Animal):
    def __init__(self, breed):
        super().__init__(breed)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks.It is a {self.breed}")


dog = Dog("Golden Retriever")
dog.speak()

 