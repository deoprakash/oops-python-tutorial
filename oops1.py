class employee:  #class initiated

    #special method/logic
    def __init__(self):
        print("Started executing data")
        self.id= 123
        self.salary = 50000
        self.designation = "SDE"
        print("data has been initiated")

    # user defined methods
    def travel(self, destination):
        print("Travel method was called manually")
        print(f"Employee is travelling to {destination}")

#create an obj/instance of class
sam = employee()
# sam.name = "Sam"
print(sam.name)
# printing attributes
# print(sam.id)

# calling method
# sam.travel('Mumbai')
