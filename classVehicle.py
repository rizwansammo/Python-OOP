class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self):
        self.y+=1
    def moveLeft(self):
        self.x-=1
    def moveRight(self):
        self.x+=1
    def moveDown(self):
        self.y-=1
    def print_position(self):
        answer=(self.x,self.y)
        print(answer)
car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()
