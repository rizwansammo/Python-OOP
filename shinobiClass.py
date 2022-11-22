# ➢ Update the number of mission from the given argument.
# ➢ If rank == 'Genin' then salary = #mission * 50
# ➢ If rank == 'Chunin' then salary = #mission * 100
# ➢ else salary = #mission * 500

class Shinobi:
  def __init__(self,name,rank):
    self.name=name
    self.rank=rank
    self.salary=0
    self.mission=0

  def changeRank(self,n_rank):
    self.rank=n_rank

  def calSalary(self,num):
    self.mission=num
    if self.rank=="Genin":
      self.salary=self.mission*50
    elif self.rank=="Chunin":
      self.salary=self.mission*100
    else:
      self.salary=self.mission*500



  def printInfo(self):
    print("Name: ",self.name)
    print("Rank: ",self.rank)
    print("Number of mission: ",self.mission)
    print("Salary:",self.salary)



naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()
