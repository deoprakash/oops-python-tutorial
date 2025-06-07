# #Single Inheritance

# #Base class

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
    
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# child = Child("Alice")
# child.greet()
# child.play()

# #...................................................

# # Multi Level inheritance

# #Base Class

# class Grandparent:
#     def __init__(self, name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} tells a story.")
    
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working.")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# child = Child("Bob")
# child.tell_story()
# child.work()
# child.play()

# # ...........................................................

# # Hierarchical inheritance 

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
    
# class Child1(Parent):
   
#     def play(self):
#         print(f"{self.name} is playing.")

# class Child2(Parent):
    
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Bob")
# child2 = Child2("Alice")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()

#.........................................................

# Multiple / Diamond Inheritance

# Common base class

# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")
    
# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}")
#         super().greet()

# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}")
#         super().greet()

# class D(B, C):
#     def greet(self):
#         print(f"Hello from D, {self.name}")
#         super().greet()

# d = D("Frank")
# d.greet()

# ....................................................

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes sound.")

# Derived class 1

class Mammal(Animal):

    def feed(self):
        print(f"{self.name} feed milk.")

# Derived class 2
 
class Bird(Animal):
   
    def fly(self):
        print(f"{self.name} is flying.")


class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()