class Item:
    pay_rate = 0.8 # Сума після знижки в 20%
    all_class_instance = list() # змінні класу


    def __init__(self, name: str, price: float, quantity=0):
        self.name = name # атрибути класу
        self.price = price  # атрибути класу
        self.quantity = quantity  # атрибути класу

        Item.all_class_instance.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def info(self):
        return f"Item( name:{self.name}, price:{self.price}, quantity:{self.quantity} )"


item1 = Item('Phone', 100, 1)
item2 = Item("Laptop", 1000, 5)


print(item1.__dict__)
item2.apply_discount()
print(item2.__dict__)
print(item2.all_class_instance)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(item1.__dict__)
# print(item2.__dict__)