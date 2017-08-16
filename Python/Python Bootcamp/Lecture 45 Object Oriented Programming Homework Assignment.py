class Line(object):
  def __init__(self, cord1, cord2):
    self.cord1 = cord1
    self.cord2 = cord2

  def distance(self):
    return ((self.cord1[0] - self.cord2[0])**2 + (self.cord1[1] - self.cord2[1])**2)**.5

  def slope(self):
    return (self.cord1[1] - self.cord2[1]) / (self.cord1[0] - self.cord2[0])

line = Line((3,2), (8,10))
print(line.distance())
print(line.slope())

class Cylinder(object):
  def __init__(self, radius = 1, height = 1):
    self.pi = 3.14159265359
    self.radius = radius
    self.height = height

  def volume(self):
    return self.height*self.pi*self.radius**2

  def surface_area(self):
    return 2*self.pi*self.radius*self.height+2*self.pi*self.radius**2

cylinder = Cylinder(4,8)
print(cylinder.volume())
print(cylinder.surface_area())