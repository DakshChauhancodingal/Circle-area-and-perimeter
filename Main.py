class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Radius is",3.14*self.radius*self.radius)
    def perimeter(self):
            print("Radius is",2*3.14*self.radius*self.radius)

obj=circle(3)
obj.area()
obj.perimeter()