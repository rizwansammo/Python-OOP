class Cat:

    def __init__(self,name=None,action=None):
        self.name=name
        self.action=action
    def printCat(self):
        if self.name==None:
            self.name='White'
        if self.action==None:
            self.action='sitting'
        print(f"{self.name} cat is {self.action}")

    def changeColor(self,color):
        self.name=color

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
