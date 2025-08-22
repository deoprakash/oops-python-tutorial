# We use @property decorator on any method in the clss to use the method as a property.

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def calcPercent(self):
        return str((self.phy + self.chem + self.maths)/3) + "%" 

stu1 = Student(45, 67, 89)
print(stu1.calcPercent)
stu1.phy = 93
print(stu1.calcPercent)

