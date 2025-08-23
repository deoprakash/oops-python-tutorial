class Area:
    def calculate(self, *args):
        if len(args) == 1: #circle
            radius = args[0]
            print("circle: ", radius * radius * (22/7))

        if len(args) == 2: #rectangle
            print("rectangle: ", args[0] * args[1])

        if len(args) == 3 :
            print("cubiod: ",args[0]*args[1]*args[2])
        else:
            return None
        
a = Area()
a.calculate(7)
a.calculate(4, 2)
a.calculate(4, 9, 6)
