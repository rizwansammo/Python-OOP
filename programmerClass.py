class Programmer:
  def __init__(self,name,lang,exp):
    self.name=name
    self.lang=lang
    self.exp=exp
  def addExp(self,add):
    print("Updating experience of Jon Snow")
    self.exp=self.exp+add
  def printDetails(self):
    print("Horray! A new programmer is born")
    print("Name: ",self.name)
    print("Language: ",self.lang)
    print("Experience: ",self.exp,"years")


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()
