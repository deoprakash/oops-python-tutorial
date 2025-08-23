class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):  # Overriding parent method
        print("Car engine is starting with key...")

class Bike(Vehicle):
    def start(self):  # Overriding parent method
        print("Bike engine is starting with self-start...")

# Testing
v = Vehicle()
v.start()

c = Car()
c.start()

b = Bike()
b.start()

# Runtime polymorphism
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
