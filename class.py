class Item:
    def calculate_total_price(self, price, quantity): # price, quantity - аргументи
        return price * quantity

item = Item() # екземпляр класу 
item.name = 'Test name'
item.price = 1000
item.quantity = 90

# print(item.name)
print(item.__dict__)
#{'name': 'Test name', 'price': 1000, 'quantity': 90}

print(item.calculate_total_price(item.price, item.quantity))
# 90000

item2 = Item()
# item2.name = 'Test name2'
item2.price = 500
item2.quantity = 45

# print(item2.name)
#
# print(item2.calculate_total_price(item2.price, item.quantity))

print(item2.__dict__)
# {'price': 500, 'quantity': 45}
