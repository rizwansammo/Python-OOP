class Student:
    def __init__(self,name=None):
        self.name=name
    def quizcalc(self,*scores):
        score=0
        for i in scores:
            score+=i
        self.avg=score/3
    def printdetail(self):
        if self.name==None:
            print(f"Hello default student\nYour average quiz score is {self.avg}")
        else:
            print(f"Hello {self.name}\nYour average quiz score is {self.avg}")




s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()
