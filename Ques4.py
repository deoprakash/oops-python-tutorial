'''Define Employee class with attribute role, department and salary. Also add showDetail().
Create an Engineer class that inherit property from Employee & has additional attribute : name & age'''

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role: ", self.role, "\n", "Department: ", self.department, "\n", "salary: ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)
    
    def information(self):
        print("name: ", self.name, "\n", "Age: ", self.age)
        print(self.showDetails())
    



e1 = Engineer("Rohan", "45", "Manager", "IT", "35000")
e1.information()
        