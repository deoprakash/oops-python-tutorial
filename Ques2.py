'''Create Account class with 2 attribute - balance and account no.
Create methods for debit, credit & printing the balance.'''

class Account: 
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("total amount: ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("total amount: ", self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, "ac12345")
acc1.debit(1000)
acc1.credit(4000)
acc1.credit(500)
acc1.debit(2500)

