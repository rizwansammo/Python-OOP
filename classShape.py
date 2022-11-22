class Shape:
  def __init__(self,name,num1,num2):
    self.name=name
    self.base=num1
    self.height=num2

  def area(self):
    if self.name=='Triangle' or self.name=='Rhombus':
      ar=.5*self.base*self.height
      print("Area: ",ar)
    elif self.name=='Rectangle':
      ar=self.base*self.height
      print("Area: ",ar)
    elif self.name=='Square':
      ar=self.base*self.height
      print("Area: ",ar)
    else:
      print('Shape Unknown')


triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()
