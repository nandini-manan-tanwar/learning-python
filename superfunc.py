#with super()

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled=is_filled
  def describe(self):
     print(f"it is {self.color} in color and {"filled" if self.is_filled else "not filled"}")
class Circle (Shape):
    def __init__(self, color, is_filled, radius):
      super().__init__(color, is_filled)
      self.radius = radius
    def describe(self):
       print(f"the area of circle is {3.14*self.radius*self.radius}")
       super().describe()


class Square (Shape):
     def __init__ (self, color, is_filled, width):
       super().__init__(color, is_filled)
       self.width = width

class Triangle(Shape):
   def __init__(self, color, is_filled, width, height):
     super().__init__(color, is_filled)
     self.width = width
     self.height = height

CircLe=Circle("pink",True,4)
print(CircLe.color)
CircLe.describe()