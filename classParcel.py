class ParcelKoro:
    def __init__(self, name="No name set", product_weight=0):
        self.name = name
        self.adress = None
        self.product_weight = product_weight
    def calculateFee(self, newloc = None):
        self.adress = newloc
        if self.product_weight == 0:
            self.fee = 0
        elif self.adress == None:
            self.fee = (self.product_weight * 20) + 50
        else:
            self.fee = (self.product_weight * 20) + 100
    def printDetails(self):
        print(f"Customer Name: {self.name} \nProduct Weight: {self.product_weight} \nTotal fee: {self.fee}")




print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()
