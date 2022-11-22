class Calculator:

  def __init__(self):
   print("Let's Calculate")

  def add(self,v1,v2):
    print("Result: ",v1+v2)

  def subtract(self,v1,v2):
    print("Result: ",va-v2)
  def multiply(self,v1,v2):
    print("Result: ",v1*v2)
  def divide(self,v1,v2):
    print("Result: ",v1/v2)

out= Calculator()
val1=int(input("Value 1: "))
op=input("Operator: ")
val2=int(input("Value 2: "))
if op=='+':
  out.add(val1,val2)
elif op=='-':
  out.subtract(val1,val2)
elif op=='/':
  out.multiply(val1,val2)
elif op=='*':
  out.divide(val1,val2)
