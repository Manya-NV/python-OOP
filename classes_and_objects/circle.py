# area and circumference of a circle
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 2*3.142*self.radius**2
    def circumference(self):
        return 2*3.142*self.radius
c1=circle(5)
c2=circle(10)
print(f"circle has area {c1.area()} and has circumference {c1.circumference()}")
print(f"circle has area {c2.area()} and has circumference {c2.circumference()}")