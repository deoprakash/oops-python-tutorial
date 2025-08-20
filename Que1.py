''' Create Student class that takes name and marks of 3 subjects as arguments in constructor. then create a method to print average'''
import math

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "Your avg score is: ", sum/3)


name = input("Enter name: "),
marks = list(map(int, input("Enter marks for 3 subjects (space separated): ").split()))

s1 = Student(name, marks)
s1.avg_marks()