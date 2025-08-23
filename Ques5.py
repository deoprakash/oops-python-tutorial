''' Create a class called Order store items & price. Under Dunder function ___gt__() to convery that:
    order1 > order2 if price of order1 > price of order2'''

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("Chips", 10)
ord2 = Order("Chocolates", 20)

print(ord1 > ord2)


        