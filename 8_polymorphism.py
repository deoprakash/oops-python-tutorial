'''When operator is allowed to have different meaning according to context. '''

''' Adding of two complex numbers'''

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")
    
    def __add__(self, num2):                # __add__ is a dunder method
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(4, 5)
num1.showNumber()

num2 = Complex(3, 9)
num2.showNumber()

num3 = num1 - num2
print(num3.showNumber())