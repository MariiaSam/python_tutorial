'''
Метод update() використовується для оновлення словника іншим словником або парами ключ-значення.
'''

my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com", "age": 26})

print(my_dict)
#{'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
