class Calculator:

  def __init__(self):
    print("Calculator is ready")


  def calculate(self,val1,val2,op):
    self.val1=val1
    self.val2=val2
    self.op=op
    self.result=0

    if op=="+":
      self.result=val1 + val2
      return self.result
    elif op=="-":
      self.result=val1 - val2
      return self.result
    elif op=="*":
      self.result=val1 * val2
      return self.result
    elif op=="/":
      self.result=val1 / val2
      return self.result

  def showCalculation(self):
    print(f"{self.val1} {self.op} {self.val2}={self.result}")




c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()
