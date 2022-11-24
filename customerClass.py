class Customer:
    def __init__(self,name):
        self.name=name

    def greet(self,person=None):
        if person==None:
            print('Hello!')
        else:
            print(f"Hello {person}")
    def purchase(self,*items):
        print(f"{self.name}, you purchaged {len(items)} item(s):")
        for i in items:
            print(i)





customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")
