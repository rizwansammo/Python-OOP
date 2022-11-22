#2
class Course:

  def __init__(self,cn,f,s):
    self.course=cn
    self.faculty=f
    self.section=str(s)

  def detail(self):

    print(self.course+"-"+self.faculty+"-"+self.section)

c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()
