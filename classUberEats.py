class UberEats:
  def __init__(self,name,phone,address):
    self.name=name
    self.phone=phone
    self.address=address
    self.item1=""
    self.item2=""
    self.price1=0
    self.price2=0
    self.item_dict={}
    print(f"{self.name}, welcome to UberEats!")

  def add_items(self,item1,item2,price1,price2):
    self.item1=item1
    self.item2=item2
    self.price1=price1
    self.price2=price2

    self.item_dict={self.item1:self.price1,self.item2:self.price2}

  def print_order_detail(self):
    return (f"Name:{self.name},Phone:{self.phone},Address:{self.address},\nOrders:{self.item_dict},\nTotal Paid: {self.price1 + self.price2}")


order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())
