class Teacher:
    def __init__(self):

        # Public - accessible from anywhere
        self.name = "Deo"
        self.subject = "Maths"

        # protected - accesible from class and subclass
        self._emp_id = 12345
        self._salary = 25000

        # Private - accessible from class only
        self.__contact = "123-456-7890"
        self.__bank_acc = "ACC123456"

    #Public method
    def teach(self):
        return f"{self.name} teaches {self.subject}"
    
    #Protected method
    def _calculate_bonus(self):
        return self._salary * 0.1

    #Private method
    def __get_personal_info(self):
        return f"Contact: {self.__contact}, Account: {self.__bank_acc}"
    

    def display_info(self):
        return self.__get_personal_info()
    

#----------------------Getter & Setter -------------------------------------------------#
    
    #Getter & Setter for protected 

    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, value):
        self._emp_id = value
    
    # Getter & Setter for private 

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, new):
        self.__contact = new


#---------------------example--------------------------

t1 = Teacher()

# Public
print("Name: ", t1.name)

# Protected use getter and setter
print("Old Emp id: ", t1.get_emp_id())
t1.set_emp_id("98765")
print("New Emp id: ", t1.get_emp_id())

# Private use getter and setter property

print("Old Conatct: ", t1.contact)
t1.contact = "6203-113-839"
print("New Conatct: ", t1.contact)

    
    