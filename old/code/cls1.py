import numpy as np

class Rectangle:
    def __init__(self, width=3, length=4):
        self.width = width
        self.length = length
    def calc_diag(self):
        self.diag = np.sqrt(self.width**2 + self.length**2)
    def calc_volume(self, height):
        self.volume = self.width * self.length * height
        self.height = height
    def calc_perimeter(self):
        return (self.width + self.length) * 2
    def calc_area(self):
        self.area = self.volume / self.height

obj1 = Rectangle(width=5,length=12)
obj2 = Rectangle()
print('obj1:width={},length={}'.format(obj1.width, obj1.length))
print('obj2:width={},length={}'.format(obj2.width, obj2.length))

obj1.calc_diag()
obj2.calc_diag()
print('obj1:diag={}'.format(obj1.diag))
print('obj2:diag={}'.format(obj2.diag))

obj1.calc_volume(height=10)
print('obj1:vollume={}'.format(obj1.volume))

perimeter = obj2.calc_perimeter()
print('obj2:perimeter={}'.format(perimeter))

obj2.calc_volume(height=5)
obj2.calc_area()
print('obj2:area={}'.format(obj2.area))
