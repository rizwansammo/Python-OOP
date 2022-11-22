class Student:

  def __init__(self,name,Id,dept,cgpa):

    self.name=name
    self.Id=Id
    self.dept=dept
    self.cgpa=cgpa

  def calculate_CGPA(self):
    summ=0
    for i in self.cgpa:
      summ=summ+i*3
    self.cgpa=summ/(len(self.cgpa*3))
  def print_details(self):
    print(f"Name: {self.name},ID: {self.Id}")
    print("Department:",self.dept)
    print("CGPA: ",self.cgpa)
#[CGPA>3.80 Highest Distinction, CGPA>3.65 High
#Distinction, CGPA>3.50 Distinction, CGPA>2.00 Satisfactory, CGPA<2.00 Can’t
#Graduate]
    if self.cgpa>3.80:
      print("Your academic standing is 'Highest Distinction'")
    elif self.cgpa>3.65:
      print("Your academic standing is 'High Distinction'")
    elif self.cgpa>3.50:
      print("Your academic standing is 'Distinction'")
    elif self.cgpa>2.00:
      print("Your academic standing is 'Satisfactory'")
    elif self.cgpa<2.00:
      print("Sorry, you cannot graduate")



s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()
