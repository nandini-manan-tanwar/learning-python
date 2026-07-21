from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

class rectangle(shape):
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2

    def area(self):
        return self.side1*self.side2

class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side
    
class pizza(circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping
        
    
   

shapes=[circle(5),square(4),rectangle(2,3),pizza("olives",8)]

for shape in shapes:
    print(f"{shape.area()}cm²")