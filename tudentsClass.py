class Student:
    def __init__(self,name,Id,dept="CSE"):
        self.name=name
        self.id=Id
        self.dept=dept
    def dailyEffort(self,hour):
        self.hour=hour
        if hour<=2:
            self.sug="Suggestion: Should give more effort!"
        elif hour<=4:
            self.sug="Suggestion: Keep up the good work!"
        else:
            self.sug="Suggestion: Excellent! Now motivate others."
    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.dept}\nDaily Effort: {self.hour} hour(s)\n{self.sug}")








harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
