class Patient:

  def __init__(self,name,age,weight,height):
    self.name=name
    self.age=age
    self.weight=weight
    self.height=height

  def printDetails(self):
    bmi=(self.weight / ((self.height/100)**2))
    print(f"Name={self.name}")
    print(f"Age={self.age}")
    print(f"Wight={self.weight}")
    print(f"height={self.height}")
    print(f"BMI={bmi}")

p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()
