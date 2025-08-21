#----------------- Single Level Inheritance ---------------------

# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car start...")
    
#     @staticmethod
#     def stop():
#         print("car Stopped...")
    
# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyota("Fortuner")
# car2 = Toyota("prius")

# print(car1.start())
# print(car1.color)
# print(car2.stop())

#----------------------------- Multi Level Inheritance -----------------------------------

# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car start...")
    
#     @staticmethod
#     def stop():
#         print("car Stopped...")
    
# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diese,")
# car1.start()


#-------------------------------- Multiple Inheritance ------------------------------------------

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#--------------------------- Super method --------------------------------------------

''' Super : parent inside inheritance.'''

class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car start..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        

car1 = Toyota("prius", "electric")
# print(car1.type)

