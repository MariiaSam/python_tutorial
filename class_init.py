
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Phone', 100, 1)  #екземпляр класу
item2 = Item("Laptop", 1000, 5) #екземпляр класу

print(item1.calculate_total_price())
print(item2.calculate_total_price())