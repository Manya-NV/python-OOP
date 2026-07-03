#area and perimeter
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

rect1=rectangle(4,6)
rect2=rectangle(4,5)
print(f"area is {rect1.area()} and perimeter is {rect1.perimeter()}")
print(f"area is {rect2.area()} and perimeter is {rect2.perimeter()}")
